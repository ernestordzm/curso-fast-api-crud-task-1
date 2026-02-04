

# La versión 2 de Pydantic, trae varios cambios de nombrados entre otros; uno de los que afecta al proyecto en la siguiente implementación que vamos a llevar a cabo para crear una paginación es la importación de genérico:

from pydantic.generics import GenericModel
# El código a emplear queda como:

# database/pagination.py

from typing import Generic, List, TypeVar

from pydantic import BaseModel, conint
# from pydantic.generics import GenericModel




class PageParams(BaseModel):
    page: conint(ge=1) = 1
    size: conint(ge=1, le=100) = 10


T = TypeVar("T")


class PagedResponseSchema(BaseModel, Generic[T]):
    """Response schema for any paged API."""

    total: int
    page: int
    size: int
    results: List[T]


def paginate(page_params: PageParams, query, ResponseSchema: BaseModel) -> PagedResponseSchema[T]:
    """Paginate the query."""

    paginated_query = query.offset((page_params.page - 1) * page_params.size).limit(page_params.size).all()

    return PagedResponseSchema(
        total=query.count(),
        page=page_params.page,
        size=page_params.size,
        # results=[ResponseSchema.from_orm(item) for item in paginated_query],
        results=[ResponseSchema.model_validate(item) for item in paginated_query],
    )
