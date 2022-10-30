from import_export import resources
from models import PackageDetail

class PackageDetailResources(resources.ModelResource):
    class Meta:
        model = PackageDetail