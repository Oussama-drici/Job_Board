import django_filters
from .models import job, category


class JobFilter(django_filters.FilterSet):
    job_type_choices = (
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
    )
    salary = django_filters.NumberFilter(lookup_expr='gte')
    title = django_filters.CharFilter(lookup_expr='contains')
    description = django_filters.CharFilter(lookup_expr='contains')
    # job_type = django_filters.MultipleChoiceFilter(
    #   choices=job_type_choices, lookup_expr='exact')
    # category = django_filters.ModelChoiceFilter(
    #   queryset=category.objects.all())

    class Meta:
        model = job
        fields = ['title',
                  'job_type',
                  'description',
                  'salary',
                  'category']
