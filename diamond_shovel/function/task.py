from typing import Callable


class TaskContext:
    ...

class TaskPipeline:
    def add(self, worker_id: str, worker: Callable[[TaskContext], None]):
        ...

    def insert_before(self, before_id: str, worker_id: str, worker: Callable[[TaskContext], None]):
        ...

    def insert_after(self, after_id: str, worker_id: str, worker: Callable[[TaskContext], None]):
        ...

    def insert_first(self, worker_id: str, worker: Callable[[TaskContext], None]):
        ...
