# This file is part of UNO Dialog Tools - UNODIT
# Copyright © 2016-2019 Sasa Kelecevic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with UNODIT.  If not, see <http://www.gnu.org/licenses/>

"""
Convert dialog file .xdl to python code and embed in document.

"""

import zipfile
import logging
import os
import shutil

try:
    from unodit import config as conf
except ImportError:
    import pythonpath.config as conf


class EmbedScript:
    def __init__(self, pydir, app="MyApp"):
        self.pydir = pydir
        self.app = app
        self.language = "python"
        self.config = conf.ReadINI(conf.MAIN_DIR, self.pydir)
        self.logger = logging.getLogger("unodit.embed_packer.EmbedScript")
        self.logger.info("NEW LOGGER: unodit.embed_packer.EmbedScript")

    def extract_document(self, fname, dest):

        fh = open(fname, "rb")
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            z.extract(name, dest)
        fh.close()

    def create_dirs(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def new_manifest_text(self, folder, macro):
        proj_name_dir = "Scripts/python/" + folder + "/"
        new_line = ""
        for path in ["Scripts/", "Scripts/python/", proj_name_dir]:
            new_line += (
                ' <manifest:file-entry manifest:full-path="%s" manifest:media-type="application/vnd.sun.star.framework-script"/>\n'
                % path
            )

        p = proj_name_dir + macro
        new_line += (
            ' <manifest:file-entry manifest:full-path="%s" manifest:media-type="application/binary"/>\n'
            % p
        )
        self.logger.info("edit manifest.xml " + new_line)
        return new_line

    def edit_manifest(self, mfs, newtext):
        doc = open(mfs, "r")
        dr = doc.read()
        newdoc = dr.replace("</manifest:manifest>", newtext)
        doc.close()

        doc = open(mfs, "w")
        doc.write(newdoc)
        doc.write("</manifest:manifest>")
        doc.close()

    def pack_script(self):

        extract_dir = os.path.join(self.pydir, "temp")
        new_dirs = os.path.join(extract_dir, "Scripts", "python", self.app)
        macro_src = os.path.join(
            self.pydir,
            self.config.get("directories", "source_dir"),
            self.app + ".py",
        )
        macro_dest = os.path.join(
            extract_dir, "Scripts", "python", self.app, self.app + ".py"
        )
        manifest_path = os.path.join(extract_dir, "META-INF", "manifest.xml")

        for file in os.listdir(self.pydir):
            if file.endswith((".odt", ".ods", ".odp", ".odg")):
                file_name = os.path.join(self.pydir, file)
                # extract document in extract dir
                self.extract_document(file_name, extract_dir)
                self.logger.info(
                    "extracted " + file_name + " in temp dir " + extract_dir
                )

                # create new scripts directories
                self.create_dirs(new_dirs)

                # copy macro
                shutil.copy(macro_src, macro_dest)

                # new manifest text
                new_mnf_dir = self.app
                new_mnf_macro = self.app + ".py"
                new_text = self.new_manifest_text(new_mnf_dir, new_mnf_macro)

                # edit manifest
                self.edit_manifest(manifest_path, new_text)

                # zip new file
                file_name_parts = file.split(".")
                new_odf = os.path.join(
                    self.pydir,
                    file_name_parts[0] + "_MACRO." + file_name_parts[1],
                )
                self.logger.info("created new odt document " + new_odf)
                zf = zipfile.ZipFile(new_odf, "w", zipfile.ZIP_DEFLATED)

                for dirname, subdirs, files in os.walk(extract_dir):
                    for filename in files:
                        fullpath = os.path.join(dirname, filename)
                        zippath = fullpath.replace(extract_dir, "")
                        self.logger.info(fullpath + "  " + zippath)
                        zf.write(fullpath, zippath, zipfile.ZIP_DEFLATED)
                zf.close()

                # remove temp dir
                shutil.rmtree(extract_dir)
                self.logger.info("removed temp dir " + extract_dir)
