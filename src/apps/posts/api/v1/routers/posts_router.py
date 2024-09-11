from rest_framework.routers import DefaultRouter, Route, DynamicRoute

class PostsRouter(DefaultRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            name='{basename}-list',
            mapping={
                'get': 'list',
                'post': 'create'
            },
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
