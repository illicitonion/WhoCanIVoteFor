from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import index, sitemap
from django.urls import include, path, re_path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from elections.sitemaps import ElectionSitemap, PostElectionSitemap
from parties.sitemaps import PartySitemap
from people.sitemaps import PersonSitemap

sitemaps = {
    "elections": ElectionSitemap,
    "postelections": PostElectionSitemap,
    "people": PersonSitemap,
    "parties": PartySitemap,
}

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        re_path(r"^i18n/", include("django.conf.urls.i18n")),
        path("", include("core.urls")),
        path("elections/", include("elections.urls")),
        path("parties/", include("parties.urls")),
        path("person/", include("people.urls")),
        path("feedback/", include("feedback.urls")),
        path("api/", include(("api.urls", "api"), namespace="api")),
        path(
            "sitemap.xml",
            cache_page(86400)(index),
            {"sitemaps": sitemaps},
        ),
        path(
            "sitemap-<section>.xml",
            cache_page(86400)(sitemap),
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap",
        ),
        re_path(
            r"^robots\.txt$",
            TemplateView.as_view(
                template_name="robots.txt", content_type="text/plain"
            ),
        ),
        path("mailing_list/", include("mailing_list.urls", "dc_signup_form")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


if settings.DEBUG:
    import debug_toolbar
    from dc_utils.urls import dc_utils_testing_patterns

    urlpatterns = (
        [path("__debug__/", include(debug_toolbar.urls))]
        + dc_utils_testing_patterns
        + urlpatterns
    )
