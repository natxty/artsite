# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('gallery_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('gallery', ['Category'])

        # Adding model 'Series'
        db.create_table('gallery_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('meta_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('gallery', ['Series'])

        # Adding model 'Work'
        db.create_table('gallery_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Series'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('depth', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_primary_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('quote', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('quote_byline', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('meta_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('gallery', ['Work'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('gallery_category')

        # Deleting model 'Series'
        db.delete_table('gallery_series')

        # Deleting model 'Work'
        db.delete_table('gallery_work')


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
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
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