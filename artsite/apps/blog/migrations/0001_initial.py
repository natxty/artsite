# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('main_content', self.gf('django.db.models.fields.TextField')()),
            ('sub_content', self.gf('django.db.models.fields.TextField')()),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('blog_post')


    models = {
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_content': ('django.db.models.fields.TextField', [], {}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sub_content': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']