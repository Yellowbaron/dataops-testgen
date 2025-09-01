from urllib.parse import quote_plus

from testgen.common.database.flavor.flavor_service import FlavorService


class ClickhouseFlavorService(FlavorService):
    def get_connection_string_head(self) -> str:
        # clickhouse+http://user:password@host:port/db
        user_pass = ""
        if self.username:
            user_pass = f"{self.username}:{quote_plus(self.password)}@"
        return f"clickhouse+http://{user_pass}"

    def get_connection_string_from_fields(self) -> str:
        # STANDARD FORMAT:  strConnect = 'flavor://username:password@host:port/database'
        return f"{self.get_connection_string_head()}{self.host}:{self.port}/{self.dbname}"
