from dataclasses import dataclass


@dataclass
class ServiceInfo:
    """微服务Jar包模型"""
    name: str
    path: str
    port: int
    status: str = "stopped"
    pid: int | None = None
    cpu: float = 0.0
    memory: float = 0.0
    description: str = ""
    group: str = "default"
    icon: str = ""

    def is_running(self) -> bool:
        return self.status == "running"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "path": self.path,
            "port": self.port,
            "status": self.status,
            "pid": self.pid,
            "cpu": self.cpu,
            "memory": self.memory,
            "description": self.description,
            "group": self.group,
            "icon": self.icon,
        }

    @staticmethod
    def from_dict(self, data: dict):
        return ServiceInfo(
            name=data.get("name", ""),
            port=data.get("port", 0),
            path=data.get("path", ""),
            status=data.get("status", "stopped"),
            pid=data.get("pid"),
            cpu=data.get("cpu", 0.0),
            memory=data.get("memory", 0.0),
            description=data.get("description", ""),
            group=data.get("group", "default"),
            icon=data.get("icon", "")
        )
