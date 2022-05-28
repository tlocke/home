Title: I'm pleased to announce the marriage of XSL and JavaScript
Date: 2006-12-13 09:29
Author: Tony Locke
Slug: im-pleased-to-announce-marriage-of-xsl
Status: published

To get an XSL stylesheet to output XML with JavaScript in it, do this:

    <?xml version="1.0" encoding="us-ascii"?>
    <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&t;
    <xsl:output method="xml"
        doctype-public="-//W3C//DTD XHTML 1.1//EN"
        doctype-system="http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"
        cdata-section-elements="javascript-escape" />

    <xsl:template match="/">
      <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
        <head>
          <title>The Marriage of XSL and JavaScript</title>
          <script type="text/javascript">

          /*
            <javascript-escape>
              <![CDATA[
          */

    function load() {
         alert("All your bases are belong to us.");
    }

          /* ]]>
            </javascript-escape>
          */
          </script>
        </head>

      <body onload="load()">
        <p>Captain: You know what you doing.</p>
      </body>
    </html>
    </xsl:template>
    </xsl:stylesheet>
