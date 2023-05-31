class Document(models.Model):
    # ...
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("reviewed", "Reviewed"),
    ]
    status = models.CharField(
        verbose_name=_("Status"),
        choices=STATUS_CHOICES,
        default="draft",
        max_length=255,
    )
    comments = models.TextField(verbose_name=_("Comments"), blank=True)
    # ...
