from app.main import app
from tests.conftest import covered_names
from fastapi.routing import APIRoute

def _route_exempt(route):
    exempt_reason: str | None = (route.openapi_extra or {}).get("x-test-exempt") 
    if exempt_reason:
        return True
    return False

def _route_covered(route): 
    return route.name in covered_names
        


def test_coverage():


    for route in app.routes:
        if not isinstance(route, APIRoute) and not type(route).__name__ == "_IncludedRouter":
            continue

        if type(route).__name__ == "_IncludedRouter":
            for sub_route in route.original_router.routes:
                if _route_exempt(sub_route):
                    continue
                assert _route_covered(sub_route),  f"Route '{sub_route.name}' has no test and is not exempt"
            continue

        if _route_exempt(route):
            continue
        
        assert _route_covered(route), f"Route '{route.name}' has no test and is not exempt"

   

