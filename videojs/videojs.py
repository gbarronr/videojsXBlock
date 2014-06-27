""" videojsXBlock main Python class"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

class videojsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    display_name = String(display_name="Display Name",
                          default="Video",
                          scope=Scope.settings,
                          help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="Video URL",
                  default="http://vjs.zencdn.net/v/oceans.mp4",
                  scope=Scope.content,
                  help="The URL for your video. This can be a YouTube URL or a link to an .mp4, .ogg, or .webm video file hosted elsewhere on the Internet.")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/videojs.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/videojs.css"))
        frag.add_javascript(self.ressource_string("static/js/video.js"))
        return frag


    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        html = self.resource_string("static/html/videojs_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/videojs_edit.js"))
        frag.initialize_js('videojsXBlock')
        return frag

    @XBlock.json_handler
    def save_videojs(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url']
        
        return {
            'result': 'success',
        }