from django.conf.urls import url

from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class


class CatalogueApplication(DashboardApplication):
    name = None

    default_permissions = ['is_staff', ]
    permissions_map = _map = {
        'catalogue-product': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-create': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-list': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-delete': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-lookup': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-category-list': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-category-create': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-class-create': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-class-list': (['is_staff'], ['partner.dashboard_access']),

    }

    product_list_view = get_class('dashboard.catalogue.views',
                                  'ProductListView')
    product_lookup_view = get_class('dashboard.catalogue.views',
                                    'ProductLookupView')
    product_create_redirect_view = get_class('dashboard.catalogue.views',
                                             'ProductCreateRedirectView')
    product_createupdate_view = get_class('dashboard.catalogue.views',
                                          'ProductCreateUpdateView')
    product_delete_view = get_class('dashboard.catalogue.views',
                                    'ProductDeleteView')

    product_class_create_view = get_class('dashboard.catalogue.views',
                                          'ProductClassCreateView')
    product_class_update_view = get_class('dashboard.catalogue.views',
                                          'ProductClassUpdateView')
    product_class_list_view = get_class('dashboard.catalogue.views',
                                        'ProductClassListView')
    product_class_delete_view = get_class('dashboard.catalogue.views',
                                          'ProductClassDeleteView')

    category_list_view = get_class('dashboard.catalogue.views',
                                   'CategoryListView')
    category_detail_list_view = get_class('dashboard.catalogue.views',
                                          'CategoryDetailListView')
    category_create_view = get_class('dashboard.catalogue.views',
                                     'CategoryCreateView')
    category_update_view = get_class('dashboard.catalogue.views',
                                     'CategoryUpdateView')
    category_delete_view = get_class('dashboard.catalogue.views',
                                     'CategoryDeleteView')

    stock_alert_view = get_class('dashboard.catalogue.views',
                                 'StockAlertListView')

    attribute_option_group_create_view = get_class('dashboard.catalogue.views',
                                                   'AttributeOptionGroupCreateView')
    attribute_option_group_list_view = get_class('dashboard.catalogue.views',
                                                 'AttributeOptionGroupListView')
    attribute_option_group_update_view = get_class('dashboard.catalogue.views',
                                                   'AttributeOptionGroupUpdateView')
    attribute_option_group_delete_view = get_class('dashboard.catalogue.views',
                                                   'AttributeOptionGroupDeleteView')

    def get_urls(self):
        urls = [
            url(r'^products/(?P<pk>\d+)/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product'),
            url(r'^products/create/$',
                self.product_create_redirect_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/create/(?P<product_class_slug>[\w-]+)/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/(?P<parent_pk>[-\d]+)/create-variant/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product-create-child'),
            url(r'^products/(?P<pk>\d+)/delete/$',
                self.product_delete_view.as_view(),
                name='catalogue-product-delete'),
            url(r'^$', self.product_list_view.as_view(),
                name='catalogue-product-list'),
            url(r'^stock-alerts/$', self.stock_alert_view.as_view(),
                name='stock-alert-list'),
            url(r'^product-lookup/$', self.product_lookup_view.as_view(),
                name='catalogue-product-lookup'),
            url(r'^categories/$', self.category_list_view.as_view(),
                name='catalogue-category-list'),
            url(r'^categories/(?P<pk>\d+)/$',
                self.category_detail_list_view.as_view(),
                name='catalogue-category-detail-list'),
            url(r'^categories/create/$', self.category_create_view.as_view(),
                name='catalogue-category-create'),
            url(r'^categories/create/(?P<parent>\d+)$',
                self.category_create_view.as_view(),
                name='catalogue-category-create-child'),
            url(r'^categories/(?P<pk>\d+)/update/$',
                self.category_update_view.as_view(),
                name='catalogue-category-update'),
            url(r'^categories/(?P<pk>\d+)/delete/$',
                self.category_delete_view.as_view(),
                name='catalogue-category-delete'),
            url(r'^product-type/create/$',
                self.product_class_create_view.as_view(),
                name='catalogue-class-create'),
            url(r'^product-types/$',
                self.product_class_list_view.as_view(),
                name='catalogue-class-list'),
            url(r'^product-type/(?P<pk>\d+)/update/$',
                self.product_class_update_view.as_view(),
                name='catalogue-class-update'),
            url(r'^product-type/(?P<pk>\d+)/delete/$',
                self.product_class_delete_view.as_view(),
                name='catalogue-class-delete'),
            url(r'^attribute-option-group/create/$',
                self.attribute_option_group_create_view.as_view(),
                name='catalogue-attribute-option-group-create'),
            url(r'^attribute-option-group/$',
                self.attribute_option_group_list_view.as_view(),
                name='catalogue-attribute-option-group-list'),
            # The RelatedFieldWidgetWrapper code does something funny with
            # placeholder urls, so it does need to match more than just a pk
            url(r'^attribute-option-group/(?P<pk>\w+)/update/$',
                self.attribute_option_group_update_view.as_view(),
                name='catalogue-attribute-option-group-update'),
            # The RelatedFieldWidgetWrapper code does something funny with
            # placeholder urls, so it does need to match more than just a pk
            url(r'^attribute-option-group/(?P<pk>\w+)/delete/$',
                self.attribute_option_group_delete_view.as_view(),
                name='catalogue-attribute-option-group-delete'),
        ]
        return self.post_process_urls(urls)


application = CatalogueApplication()
