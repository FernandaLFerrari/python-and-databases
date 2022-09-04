from unittest.mock import Mock

obj = Mock()
obj.method()
obj.method.assert_called_once()