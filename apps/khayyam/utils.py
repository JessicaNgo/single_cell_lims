"""
Created on Oct 20, 2016

@author: Jafar Taghiyar (jtaghiyar@bccrc.ca)
"""

import os, sys
import subprocess as sub
import logging
# import pandas as pd 
# from string import Template

#============================
# Django imports
#----------------------------
# from .models import SublibraryInformation
from django.conf import settings


logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.DEBUG
    )


#==================================================
# Kronos initilaization and run
#--------------------------------------------------
def get_samples_file(data, *args, **kwargs):
    """make a samples file and save it in temporary working directory."""
    return "/path/foo.text"


class FileHandler(object):

    """
    Handles all the file/dir operations.
    """

    def __init__(self):
        """initialize."""
        self.wd_root = settings.WORKING_DIR_ROOT
        self.rd_root = settings.RESULTS_DIR_ROOT

    def make_tmp_wd(self, dir_name):
        """make a temporary working dir."""
        print "making temporary working directory ..."
        path = os.path.join(self.wd_root, dir_name)
        os.makedirs(path)

    def make_tmp_rd(self, dir_name):
        """make a temporary results dir."""
        pass

    def copy_wf(self, wf_name, wf_version, dir_name):
        """copy the workflow in the given directory."""
        pass

    def rsync(self, spath, dpath):
        """rcync from source to destination."""
        pass

    def rmdir(self, dirpath):
        """remove directory."""
        pass

    def clone(self, repo, dpath):
        """clone the given repository in the destination path."""
        pass

    def create_virtenv(self, reqs):
        """create a python virtualenv usgin the given requirements."""
        pass


class Kronos(object):
    
    """
    Kronos manager.
    """

    def __init__(self, workflow_instance):
        """initialize."""
        self.workflow = workflow_instance
        self.script_template = None

        self.components_dir = None
        self.drmaa_library_path = None
        self.python_installation = None

    def init(self):
        """initialize the workflow."""
        pass

    def run(self):
        """run the workflow."""
        pass

    def make_script(self):
        """make the executable run script."""
        pass

    def picasso_hand_shake(self):
        """interface to Picasso app."""
        pass
