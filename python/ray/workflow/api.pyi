# fmt: off
from typing import Callable, Generic, Optional, TypeVar, Union, overload, Any
from types import FunctionType

from ray._raylet import ObjectRef
from ray.remote_function import RemoteFunction
from ray.workflow.storage import Storage

from ray.workflow.virtual_actor_class import VirtualActorClass, VirtualActor
from ray.workflow.common import WorkflowStatus

from ray.experimental.dag import DAGNode

T0 = TypeVar("T0")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
T5 = TypeVar("T5")
T6 = TypeVar("T6")
T7 = TypeVar("T7")
T8 = TypeVar("T8")
T9 = TypeVar("T9")
R = TypeVar("R")


class Workflow(Generic[R]):
    def run(self, workflow_id: Optional[str]=None, storage: Optional[Union[Storage, str]]=None) -> R: ...
    def run_async(self, workflow_id: Optional[str]=None, storage: Optional[Union[Storage, str]]=None) -> ObjectRef[R]: ...


class WorkflowStepFunction(Generic[R, T0, T1, T2, T3, T4, T5, T6, T7, T8, T9]):
    def __init__(self, function: Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9], R]) -> None: pass

    @overload
    def step(self) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]], arg4: Union[T4, ObjectRef[T4], Workflow[T4]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]], arg4: Union[T4, ObjectRef[T4], Workflow[T4]], arg5: Union[T5, ObjectRef[T5], Workflow[T5]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]], arg4: Union[T4, ObjectRef[T4], Workflow[T4]], arg5: Union[T5, ObjectRef[T5], Workflow[T5]], arg6: Union[T6, ObjectRef[T6], Workflow[T6]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]], arg4: Union[T4, ObjectRef[T4], Workflow[T4]], arg5: Union[T5, ObjectRef[T5], Workflow[T5]], arg6: Union[T6, ObjectRef[T6], Workflow[T6]], arg7: Union[T7, ObjectRef[T7], Workflow[T7]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]], arg4: Union[T4, ObjectRef[T4], Workflow[T4]], arg5: Union[T5, ObjectRef[T5], Workflow[T5]], arg6: Union[T6, ObjectRef[T6], Workflow[T6]], arg7: Union[T7, ObjectRef[T7], Workflow[T7]], arg8: Union[T8, ObjectRef[T8], Workflow[T8]]) -> Workflow[R]: ...
    @overload
    def step(self, arg0: Union[T0, ObjectRef[T0], Workflow[T0]], arg1: Union[T1, ObjectRef[T1], Workflow[T1]], arg2: Union[T2, ObjectRef[T2], Workflow[T2]], arg3: Union[T3, ObjectRef[T3], Workflow[T3]], arg4: Union[T4, ObjectRef[T4], Workflow[T4]], arg5: Union[T5, ObjectRef[T5], Workflow[T5]], arg6: Union[T6, ObjectRef[T6], Workflow[T6]], arg7: Union[T7, ObjectRef[T7], Workflow[T7]], arg8: Union[T8, ObjectRef[T8], Workflow[T8]], arg9: Union[T9, ObjectRef[T9], Workflow[T9]]) -> Workflow[R]: ...
    @overload
    def step(self, *args, **kwargs) -> Workflow[R]: ...


@overload
def step(function: Callable[[], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, None, None, None, None, None, None, None, None, None, None]: ...
@overload
def step(function: Callable[[T0], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, None, None, None, None, None, None, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, None, None, None, None, None, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, None, None, None, None, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, None, None, None, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3, T4], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, None, None, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3, T4, T5], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, T5, None, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3, T4, T5, T6], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, T5, T6, None, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3, T4, T5, T6, T7], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, T5, T6, T7, None, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, T5, T6, T7, T8, None]: ...
@overload
def step(function: Callable[[T0, T1, T2, T3, T4, T5, T6, T7, T8, T9], Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, T5, T6, T7, T8, T9]: ...
@overload
def step(function: Callable[..., Union[R, Workflow[R]]]) -> WorkflowStepFunction[R, T0, T1, T2, T3, T4, T5, T6, T7, T8, T9]: ...

@overload
def resume(workflow_id: str) -> ObjectRef: ...
@overload
def resume(workflow_id: str) -> ObjectRef: ...

class _VirtualActorDecorator:
    @classmethod
    def __call__(cls, _cls: type) -> "VirtualActorClass": ...
    @classmethod
    def readonly(cls, method: FunctionType) ->  FunctionType: ...

virtual_actor: _VirtualActorDecorator

def get_output(workflow_id: str, name: str) -> ObjectRef: ...

def list_all(status_filter: Optional[Union[WorkflowStatus, Set[WorkflowStatus]]]) -> List[Tuple[str, WorkflowStatus]]: ...

def resume_all(include_failed: bool) -> List[str]: ...

def get_status(workflow_id: str) -> WorkflowStatus: ...

def wait_for_event(event_listener_type: EventListenerType, *args, **kwargs) -> DAGNode: ...

def sleep(duration: float) -> DAGNode: ...

@overload
def get_metadata(workflow_id: str) -> Dict[str, Any]: ...

@overload
def get_metadata(workflow_id: str, name: str) -> Dict[str, Any]: ...

def cancel(workflow_id: str) -> None: ...

def delete_workflow(worfkflow_id: str) -> None: ...

def get_actor(actor_id: str) -> VirtualActor: ...

def init(storage: Optional[Union[str, Storage]] = None) -> None: ...

def options(**workflow_options: Dict[str, Any]) -> Callable[[RemoteFunction], RemoteFunction]: ...

def _ensure_workflow_initialized() -> None: ...
