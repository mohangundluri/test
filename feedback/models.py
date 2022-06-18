from django.db import models

class FeedbackModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(null=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_consent = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} {self.email} {self.created_at}"