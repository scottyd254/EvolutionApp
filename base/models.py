from django.db import models

# Create your models here.
# base content for navigation and footer content 

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, PublishingPanel
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
# import register_snippet:
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField


@register_snippet
class FooterContent(
    TranslatableMixin,
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model
):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Portrait mode only, recommended at least 300 x 300 px Transparent Background",
    )
    heading_title = RichTextField(blank=True)
    footer_body = RichTextField(blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("heading_title"),
        FieldPanel("footer_body"),
        PublishingPanel(),
    ]
    

    def __str__(self):
        return f"{self.heading_title}, {self.footer_body}, {self.image}"

    def get_preview_template(self, request, mode_name):
        return "base.html"
    
    def get_preview_context(self, request, mode_name):
        return {
            "heading_title": self.heading_title,
            "footer_body": self.footer_body,
            "image": self.image
        }

    class Meta(TranslatableMixin.Meta):
        verbose_name = "footer content"
        verbose_name_plural = "footer contents"

@register_setting
class FooterContentSetting(BaseGenericSetting):
    footer_content = models.ForeignKey(
        "FooterContent",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [
        FieldPanel("footer_content"),
    ]

@register_setting
class NavigationContentSetting(BaseGenericSetting):
    facebook_url = models.URLField(verbose_name="Facebook Profile Link" , null=True, blank=True)
    whatsapp_url = models.URLField(verbose_name="Whatsapp Group URL" , null=True, blank=True)
    twitter_url = models.URLField(verbose_name="Twitter Profile Link" , null=True, blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn Profile Link" , null=True, blank=True)
    instagram_url = models.URLField(verbose_name="Instagram Profile Link" , null=True, blank=True)
    youtube_url = models.URLField(verbose_name="Youtube Profile Link" , null=True, blank=True)
    panels = [
       MultiFieldPanel([
        FieldPanel("facebook_url"),
        FieldPanel("whatsapp_url"),
        FieldPanel("twitter_url"),
        FieldPanel("linkedin_url"),
        FieldPanel("instagram_url"),
        FieldPanel("youtube_url"),
       ], heading="Social-Media Links")
    ]

