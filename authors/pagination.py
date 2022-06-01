from rest_framework.pagination import LimitOffsetPagination


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class BiographyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
