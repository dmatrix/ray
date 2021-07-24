// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

#pragma once

#include "absl/container/flat_hash_set.h"
#include "gtest/gtest.h"
#include "ray/object_manager/plasma/common.h"
#include "ray/object_manager/plasma/eviction_policy.h"
#include "ray/object_manager/plasma/object_store.h"
#include "ray/object_manager/plasma/plasma_allocator.h"

namespace plasma {

// ObjectLifecycleManager allocates LocalObjects from the allocator.
// It tracks object’s lifecycle states including reference_count and created/sealed.
// It uses eviction_policy to garbage collect objects when running out of space.
class ObjectLifecycleManager {
 public:
  ObjectLifecycleManager(IAllocator &allocator,
                         ray::DeleteObjectCallback delete_object_callback);

  /// Create a new object given object's info. Object creation might
  /// fail if runs out of space; or an object with the same id exists.
  ///
  /// \param object_info Plasma object info.
  /// \param source From where the object is created.
  /// \param fallback_allocator Whether to allow fallback allocation.
  /// \return
  ///   - pointer to created object and PlasmaError::OK when succeeds.
  ///   - nullptr and error message, including ObjectExists/OutOfMemory
  std::pair<const LocalObject *, flatbuf::PlasmaError> CreateObject(
      const ray::ObjectInfo &object_info, plasma::flatbuf::ObjectSource source,
      bool fallback_allocator);

  /// Get object by id.
  /// \return
  ///   - nullptr if such object doesn't exist.
  ///   - otherwise, pointer to the object.
  const LocalObject *GetObject(const ObjectID &object_id) const;

  /// Seal created object by id.
  ///
  /// \param object_id Object ID of the object to be sealed.
  /// \return
  ///   - nulltpr if such object doesn't exist, or the object has already been sealed.
  ///   - otherise, pointer to the sealed object.
  const LocalObject *SealObject(const ObjectID &object_id);

  /// Abort object creation by id. It deletes the object regardless of reference
  /// counting.
  ///
  /// \param object_id Object ID of the object to be aborted.
  /// \return
  ///   - false if such object doesn't exist, or the object has already been sealed.
  ///   - true if abort successfuly.
  bool AbortObject(const ObjectID &object_id);

  /// Delete a specific object by object_id. The object is delete immediately
  /// if it's been sealed and reference counting is zero. Otherwise it will not
  /// be deleted.
  ///
  /// \param object_id Object ID of the object to be deleted.
  /// \return One of the following error codes:
  ///  - PlasmaError::OK, if the object was delete successfully.
  ///  - PlasmaError::ObjectNonexistent, if ths object isn't existed.
  ///  - PlasmaError::ObjectNotsealed, if ths object is created but not sealed.
  ///  - PlasmaError::ObjectInUse, if the object is in use; it will be deleted
  ///  once it's no longer used (ref count becomes 0).
  flatbuf::PlasmaError DeleteObject(const ObjectID &object_id);

  /// Bump up the reference count of the object.
  ///
  /// \return true if object exists, false otherise.
  bool AddReference(const ObjectID &object_id);

  /// Decrese the reference count of the object. When reference count
  /// drop to zero the object becomes evictable.
  ///
  /// \return true if object exists and reference count is greater than 0, false otherise.
  bool RemoveReference(const ObjectID &object_id);

  /// Ask it to evict objects until we have at least size of capacity
  /// available.
  /// TEST ONLY
  ///
  /// \return The number of bytes evicted.
  int64_t RequireSpace(int64_t size);

  std::string EvictionPolicyDebugString() const;

  bool IsObjectSealed(const ObjectID &object_id) const;

  int64_t GetNumBytesInUse() const;

  int64_t GetNumBytesCreatedTotal() const;

  int64_t GetNumBytesUnsealed() const;

  int64_t GetNumObjectsUnsealed() const;

  void GetDebugDump(std::stringstream &buffer) const;

 private:
  // Test only
  ObjectLifecycleManager(std::unique_ptr<IObjectStore> store,
                         std::unique_ptr<IEvictionPolicy> eviction_policy,
                         ray::DeleteObjectCallback delete_object_callback);

  const LocalObject *CreateObjectInternal(const ray::ObjectInfo &object_info,
                                          plasma::flatbuf::ObjectSource source,
                                          bool allow_fallback_allocation);

  // Evict objects returned by the eviction policy.
  //
  // \param object_ids Object IDs of the objects to be evicted.
  void EvictObjects(const std::vector<ObjectID> &object_ids);

  void DeleteObjectInternal(const ObjectID &object_id);

 private:
  friend struct ObjectLifecycleManagerTest;
  FRIEND_TEST(ObjectLifecycleManagerTest, DeleteFailure);
  FRIEND_TEST(ObjectLifecycleManagerTest, RemoveReferenceOneRefEagerlyDeletion);

  std::unique_ptr<IObjectStore> object_store_;
  std::unique_ptr<IEvictionPolicy> eviction_policy_;
  const ray::DeleteObjectCallback delete_object_callback_;

  // list of objects which will be removed immediately
  // once reference counting boecomes 0.
  absl::flat_hash_set<ObjectID> eargerly_deletion_objects_;

  // Total bytes of the objects whose references are greater than 0.
  int64_t num_bytes_in_use_;
};

}  // namespace plasma
