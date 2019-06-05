# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeocubesPlugin
                                 A QGIS plugin
 Interface to download raster data from GeoCubes Finland
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-04
        copyright            : (C) 2019 by Paikkatietokeskus FGI
        email                : lassi.lehto@nls.fi
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeocubesPlugin class from file GeocubesPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geocubes_plugin import GeocubesPlugin
    return GeocubesPlugin(iface)