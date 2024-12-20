# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Needed Schools
                                 A QGIS plugin
 This plugin accesses the number of schools required to be added to a particular school depending on the population
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-11-30
        copyright            : (C) 2024 by bsc-inf-08-20
        email                : bsc-inf-08-20@unima.ac.mw
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
def classFactory(iface):
    from .needed_schools import NeededSchools
    return NeededSchools(iface)
