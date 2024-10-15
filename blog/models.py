from django.db import models
from django import forms

from modelcluster.models import ParentalKey, ParentalManyToManyField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField
from wagtail.search import index
# add tags to blog posts 
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

# Create your models here.
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


# add tags to posts 
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

# blog page model
class BlogPage(Page):
    published_date = models.DateField('publish date', blank=True, null=True)
    intro = models.CharField(max_length=200)
    body = RichTextField(blank=True)
    
    # add authors
    authors = ParentalManyToManyField('blog.Author', blank=True)

    # add tags
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    # add search fields published data, intro, and body
    search_fields = Page.search_fields + [
        index.SearchField('published_date'),
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("published_date"),
            FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags')
        ], heading="Blog information"),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
# add blog page image gallery to the model 
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, 
                       on_delete=models.CASCADE,
                       related_name='gallery_images')
    
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=200, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

# add authors to the model 
@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Add an author image: 16:9 ratio recommended: cropped to 300 x 300 px or less",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("author_image"),
    ]

    def __str__(self):
        self.name

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

# add a blog tag index page to the model
class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
