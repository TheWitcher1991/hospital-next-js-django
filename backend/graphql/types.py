from graphene_django import DjangoObjectType

from core.models import Cabinet, PatientType, Position
from core.models import ServiceType as ServiceCategory
from employee.models import Employee, Service


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class PatientTypeType(DjangoObjectType):
    class Meta:
        model = PatientType


class ServiceCategoryType(DjangoObjectType):
    class Meta:
        model = ServiceCategory


class PositionType(DjangoObjectType):
    class Meta:
        model = Position


class CabinetType(DjangoObjectType):
    class Meta:
        model = Cabinet


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
