from rest_framework.routers import Route, DefaultRouter, DynamicRoute


class UsersRouter(DefaultRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            name='{basename}-list',
            mapping={
                'get': 'list'
            },
            detail=False,
            initkwargs={}
        ),
        DynamicRoute(
            url=r'^{prefix}/{url_path}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            name='{basename}-detail',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            detail=True,
            initkwargs={}
        )
    ]
