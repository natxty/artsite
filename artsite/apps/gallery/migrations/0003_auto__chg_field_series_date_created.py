# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Series.date_created'
        db.alter_column('gallery_series', 'date_created', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Series.date_created'
        db.alter_column('gallery_series', 'date_created', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'gallery.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'gallery.series': {
            'Meta': {'object_name': 'Series'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Category']"}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'gallery.work': {
            'Meta': {'ordering': "['order']", 'object_name': 'Work'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_primary_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quote_byline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Series']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']