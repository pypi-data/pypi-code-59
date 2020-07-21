import uuid
from django import forms
from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Table(models.Model):
    name = models.CharField(max_length=50, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    last_update_at = models.DateTimeField()
    n_rows = models.BigIntegerField()
    n_cols = models.BigIntegerField()
    active = models.BooleanField(default=True)


class TableColumnsSpec(models.Model):
    feature_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    column_name = models.CharField(max_length=50)
    label = models.BooleanField()
    problem_type = models.CharField(max_length=30, choices=[('classification', 'classification'),
                                                            ('regression', 'regression')])
    feature = models.BooleanField()
    categorical = models.BooleanField()
    num_categories = models.IntegerField(blank=True, null=True)
    numerical = models.BooleanField()
    cluster = models.CharField(max_length=15, blank=True, null=True)
    prop_null = models.FloatField()
    distinct_values =  models.IntegerField(null=True)


class Run(models.Model):
    run_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    started_at = models.DateTimeField()
    last_update_at = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    problem_type = models.CharField(max_length=30)
    filter = models.CharField(max_length=100)
    metric = models.CharField(max_length=30)
    selection_method = models.CharField(max_length=20, blank=True, null=True)
    features = models.TextField()
    selected_features = models.TextField()
    oversampling = models.BooleanField()
    n_test = models.IntegerField()
    n_train = models.IntegerField()


class MLModel(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    optimized = models.BooleanField()
    hyperparameters = models.TextField()


class Sustainability(models.Model):
    model = models.OneToOneField(MLModel, on_delete=models.CASCADE, primary_key=True)
    carbon_footprint = models.DecimalField(max_digits=5, decimal_places=3)


class ModelContingencyTable(models.Model):
    model = models.OneToOneField(MLModel, on_delete=models.CASCADE, primary_key=True)
    true_positive = models.BigIntegerField(blank=True, null=True)
    true_negative = models.BigIntegerField(blank=True, null=True)
    false_positive = models.BigIntegerField(blank=True, null=True)
    false_negative = models.BigIntegerField(blank=True, null=True)


class ModelMetrics(models.Model):
    model = models.OneToOneField(MLModel, on_delete=models.CASCADE, primary_key=True)
    roc_auc = models.FloatField(blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)
    balanced_accuracy = models.FloatField(blank=True, null=True)
    recall = models.FloatField(blank=True, null=True)
    precision = models.FloatField(blank=True, null=True)
    f1_score = models.FloatField(blank=True, null=True)
    gini = models.FloatField(blank=True, null=True)
    log_loss = models.FloatField(blank=True, null=True)

    mean_squared_error = models.FloatField(blank=True, null=True)
    mean_absolute_error = models.FloatField(blank=True, null=True)
    r_squared = models.FloatField(blank=True, null=True)


class ModelFeatureImportance(models.Model):
    feature_importance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
    feature = models.CharField(max_length=50)
    importance = models.FloatField()
