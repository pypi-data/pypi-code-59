# -*- coding: utf-8 -*-
#############################################################################
##
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
## Contact: http:#www.qt-project.org/legal
##
## This file is part of the Qt Solutions component.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################
import sys
sys.path.append('QtProperty')
sys.path.append('libqt5')
from array import array
from PyQt5.QtGui import QTransform as QMatrix
from PyQt5.QtCore import (
    Qt, 
    QRect, 
    QTimer, 
    QPoint, 
    QSize, 
    qWarning, 
    QRectF, 
    pyqtSignal, 
    QObject
)
from PyQt5.QtGui import (
    QRegion, 
    QImage, 
    QPolygon, 
    QPixmap, 
    QPainter, 
    QPainterPath, 
    QPen, 
    QBrush, 
    QFontMetrics, 
    QFont, 
    QColor
)
from PyQt5.QtWidgets import (
    QWidget,
    QApplication, 
    QScrollArea
)
from pyqtcore import QSet, QList
from enum import Enum

class QPolygonEx(QPolygon):
    def resize(self, n):
        _n = self.size()
        for i in range(n-_n):
            self.append(QPoint())
        for i in range(_n-n):
            self.remove(self.size()-1)

    def detach(self):
        pass

def qt_testCollision(s1, s2):
    s2image = s2.imageAdvanced().collision_mask
    s2area = s2.boundingRectAdvanced()

    cyourarea = QRect(s2area.x(), s2area.y(), s2area.width(), s2area.height())

    s1image = s1.imageAdvanced().collision_mask

    s1area = s1.boundingRectAdvanced()

    ourarea = s1area.intersected(cyourarea)

    if (ourarea.isEmpty()):
        return False

    x2 = ourarea.x()-cyourarea.x()
    y2 = ourarea.y()-cyourarea.y()
    x1 = ourarea.x()-s1area.x()
    y1 = ourarea.y()-s1area.y()
    w = ourarea.width()
    h = ourarea.height()

    if (not s2image):
        if (not s1image):
            return w>0 and h>0
        # swap everything around
        t = x1; x1 = x2; x2 = t
        t = y1; x1 = y2; y2 = t
        s2image = s1image
        s1image = 0

    # s2image != 0

    # A non-linear search may be more efficient.
    # Perhaps spiralling out from the center, or a simpler
    # vertical expansion from the centreline.

    # We assume that sprite masks don't have
    # different bit orders.
    #
    # Q_ASSERT(s1image.bitOrder() == s2image.bitOrder())

    if (s1image):
        if (s1image.format() == QImage.Format_MonoLSB):
            for j in range(h):
                ml = s1image.scanLine(y1+j)
                yl = s2image.scanLine(y2+j)
                for i in range(w):
                    if (yl + ((x2+i) >> 3) & (1 << ((x2+i) & 7)) and ml + ((x1+i) >> 3) & (1 << ((x1+i) & 7))):
                        return True
        else:
            for j in range(h):
                ml = s1image.scanLine(y1+j)
                yl = s2image.scanLine(y2+j)
                for i in range(w):
                    if (yl + ((x2+i) >> 3) & (1 << (7-((x2+i) & 7))) and ml + ((x1+i) >> 3) & (1 << (7-((x1+i) & 7)))):
                        return True
    else:
        if (s2image.format() == QImage.Format_MonoLSB):
            for j in range(h):
                yl = s2image.scanLine(y2+j)
                for i in range(w):
                    if ((yl + ((x2+i) >> 3)) & (1 << ((x2+i) & 7))):
                        return True
        else:
            for j in range(h):
                yl = s2image.scanLine(y2+j)
                for i in range(w):
                    if ((yl + ((x2+i) >> 3)) & (1 << (7-((x2+i) & 7)))):
                        return True

    return False

def collision_double_dispatch(s1, p1, r1, e1, t1, s2, p2, r2, e2, t2):
    if s1:
        i1 = s1
    elif p1:
        i1 = p1
    elif r1:
        i1 = r1
    elif e1:
        i1 = e1
    elif t1:
        i1 = t1
    if s2:
        i2 = s2
    elif p2:
        i2 = p2
    elif r2:
        i2 = r2
    elif e2:
        i2 = e2
    elif t2:
        i2 = t2

    if (s1 and s2):
        # a
        return qt_testCollision(s1, s2)
    elif ((r1 or t1 or s1) and (r2 or t2 or s2)):
        # b
        rc1 = i1.boundingRectAdvanced()
        rc2 = i2.boundingRectAdvanced()
        return rc1.intersects(rc2)
    elif (e1 and e2
                and e1.angleLength()>= 360*16 and e2.angleLength()>= 360*16
                and e1.width() == e1.height()
                and e2.width() == e2.height()):
        # c
        xd = (e1.x()+e1.xVelocity())-(e2.x()+e1.xVelocity())
        yd = (e1.y()+e1.yVelocity())-(e2.y()+e1.yVelocity())
        rd = (e1.width()+e2.width())/2
        return xd*xd+yd*yd <= rd*rd
    elif (p1 and (p2 or s2 or t2)):
        # d
        pa1 = p1.areaPointsAdvanced()
        if p2:
            pa2 = p2.areaPointsAdvanced()
        else:
            pa2 = QPolygonEx(i2.boundingRectAdvanced())
        col = not (QRegion(pa1) & QRegion(pa2, Qt.WindingFill)).isEmpty()

        return col
    else:
        return collision_double_dispatch(s2, p2, r2, e2, t2, 
                                         s1, p1, r1, e1, t1)

class Edge(Enum):
    Left = 1
    Right = 2
    Top = 4
    Bottom = 8

###
#    \enum RttiValues
#
#    This enum is used to name the different types of canvas item.
#
#    \value Rtti_Item Canvas item abstract base class
#    \value Rtti_Ellipse
#    \value Rtti_Line
#    \value Rtti_Polygon
#    \value Rtti_PolygonalItem
#    \value Rtti_Rectangle
#    \value Rtti_Spline
#    \value Rtti_Sprite
#    \value Rtti_Text
#
###
class RttiValues(Enum):
    Rtti_Item = 0
    Rtti_Sprite = 1
    Rtti_PolygonalItem = 2
    Rtti_Text = 3
    Rtti_Polygon = 4
    Rtti_Rectangle = 5
    Rtti_Ellipse = 6
    Rtti_Line = 7
    Rtti_Spline = 8

class QtCanvasData():
    def __init__(self):
        self.viewList = QList()
        self.itemDict = QSet()
        self.animDict = QSet()

class QtCanvasViewData():
    def __init__(self):
        self.xform = QMatrix()
        self.ixform = QMatrix()
        self.highQuality = False

def include(r, rect):
    if (rect.left() < r.left()):
        r.setLeft(rect.left())
    if (rect.right()>r.right()):
        r.setRight(rect.right())
    if (rect.top() < r.top()):
        r.setTop(rect.top())
    if (rect.bottom()>r.bottom()):
        r.setBottom(rect.bottom())

###
#A QtCanvasClusterizer groups rectangles (QRects) into non-overlapping rectangles
#by a merging heuristic.
###
class QtCanvasClusterizer():
    def __init__(self, maxclusters):
        self.cluster = QList()
        for i in range(maxclusters):
            self.cluster.append(QRect())
        self.count = 0
        self.maxcl = maxclusters

    def __del__(self):
        del self.cluster

    def clear(self):
        self.count = 0

    def add(self, x, y, w=1, h=1):
        self.__add(QRect(x, y, w, h))

    def __add(self, rect):
        biggerrect = QRect(rect.x()-1, rect.y()-1, rect.width()+2, rect.height()+2)

        #assert(rect.width()>0 and rect.height()>0)
        for cursor in range(self.count):
            if (self.cluster[cursor].contains(rect)):
                # Wholly contained already.
                return

        lowestcost = 9999999
        cheapest = -1
        cursor = 0
        while(cursor < self.count):
            if (self.cluster[cursor].intersects(biggerrect)):
                larger = self.cluster[cursor]
                include(larger, rect)
                cost = larger.width()*larger.height() - self.cluster[cursor].width()*self.cluster[cursor].height()

                if (cost < lowestcost):
                    bad = False
                    for c in range(self.count):
                        if not bad:
                            bad = self.cluster[c].intersects(larger) and c!= cursor
                    if (not bad):
                        cheapest = cursor
                        lowestcost = cost
            cursor += 1

        if (cheapest>= 0):
            include(self.cluster[cheapest], rect)
            return

        if (self.count < self.maxcl):
            self.cluster[self.count] = rect
            self.count += 1
            return

        # Do cheapest of:
        #     add to closest self.cluster
        #     do cheapest self.cluster merge, add to new self.cluster

        lowestcost = 9999999
        cheapest = -1
        cursor = 0
        while(cursor < self.count):
            larger = self.cluster[cursor]
            include(larger, rect)
            cost = larger.width()*larger.height() - self.cluster[cursor].width()*self.cluster[cursor].height()
            if (cost < lowestcost):
                bad = False
                for c in range(self.count):
                    if not bad:
                        bad = self.cluster[c].intersects(larger) and c!= cursor
                if (not bad):
                    cheapest = cursor
                    lowestcost = cost
            cursor += 1

        # ###
        # could make an heuristic guess as to whether we need to bother
        # looking for a cheap merge.

        cheapestmerge1 = -1
        cheapestmerge2 = -1

        merge1 = 0
        while(merge1 < self.count):
            merge2 = 0
            while(merge2 < self.count):
                if(merge1!= merge2):
                    larger = self.cluster[merge1]
                    include(larger, self.cluster[merge2])
                    cost = larger.width()*larger.height() - self.cluster[merge1].width()*self.cluster[merge1].height()
                    if (cost < lowestcost):
                        bad = False
                        for c in range(self.count):
                            if not bad:
                                bad = self.cluster[c].intersects(larger) and c!= cursor
                        if (not bad):
                            cheapestmerge1 = merge1
                            cheapestmerge2 = merge2
                            lowestcost = cost
                merge2 += 1
            merge1 += 1

        if (cheapestmerge1>= 0):
            include(self.cluster[cheapestmerge1], self.cluster[cheapestmerge2])
            self.cluster[cheapestmerge2] = self.cluster[self.count]
            self.count -= 1
        else:
            # if (not cheapest) debugRectangles(rect):
            include(self.cluster[cheapest], rect)

        # NB: clusters do not intersect (or intersection will
        #     overwrite). This is a result of the above algorithm,
        #     given the assumption that (x, y) are ordered topleft
        #     to bottomright.

        # ###
        #
        # add explicit x/y ordering to that comment, move it to the top
        # and rephrase it as pre-/post-conditions.

    def __getItem__(self, i):
        return self.cluster[i]

# end of clusterizer

class QtCanvasItemLess():
    def func(self, i1, i2):
        if (i1.z() == i2.z()):
            return i1 > i2
        return (i1.z() > i2.z())

class QtCanvasChunk():
    def __init__(self):
        self.changed = True
        self.m_list = QList()
    # Other code assumes lists are not deleted. Assignment is also
    # done on ChunkRecs. So don't add that sort of thing here.

    def sort(self):
        self.m_list = QList(sorted(self.m_list, key=lambda x:x.z(), reverse=True))

    def list(self):
        return self.m_list

    def add(self, item):
        self.m_list.prepend(item)
        self.changed = True

    def remove(self, item):
        self.m_list.removeAll(item)
        self.changed = True

    def change(self):
        self.changed = True

    def hasChanged(self):
        return self.changed

    def takeChange(self):
        y = self.changed
        self.changed = False
        return y

def gcd(a, b):
    r = 0
    while r:
        r = a%b
        a = b
        b = r
    return b

def scm(a, b):
    g = gcd(a, b)
    return a/g*b

###
#    \class QtCanvas qtcanvas.h
#    \brief The QtCanvas class provides a 2D area that can contain QtCanvasItem objects.
#
#    The QtCanvas class manages its 2D graphic area and all the canvas
#    items the area contains. The canvas has no visual appearance of
#    its own. Instead, it is displayed on screen using a QtCanvasView.
#    Multiple QtCanvasView widgets may be associated with a canvas to
#    provide multiple views of the same canvas.
#
#    The canvas is optimized for large numbers of items, particularly
#    where only a small percentage of the items change at any
#    one time. If the entire display changes very frequently, you should
#    consider using your own custom QtScrollView subclass.
#
#    Qt provides a rich
#    set of canvas item classes, e.g. QtCanvasEllipse, QtCanvasLine,
#    QtCanvasPolygon, QtCanvasPolygonalItem, QtCanvasRectangle, QtCanvasSpline,
#    QtCanvasSprite and QtCanvasText. You can subclass to create your own
#    canvas items; QtCanvasPolygonalItem is the most common base class used
#    for this purpose.
#
#    Items appear on the canvas after their \link QtCanvasItem.show()
#    show()\endlink function has been called (or \link
#    QtCanvasItem.setVisible() setVisible(True)\endlink), and \e after
#    update() has been called. The canvas only shows items that are
#    \link QtCanvasItem.setVisible() visible\endlink, and then only if
#    \l update() is called. (By default the canvas is white and so are
#    canvas items, so if nothing appears try changing colors.):
#
#    If you created the canvas without passing a width and height to
#    the constructor you must also call resize().
#
#    Although a canvas may appear to be similar to a widget with child
#    widgets, there are several notable differences:
#
#    \list
#    \i Canvas items are usually much faster to manipulate and redraw than
#    child widgets, with the speed advantage becoming especially great when
#    there are \e many canvas items and non-rectangular items. In most
#    situations canvas items are also a lot more memory efficient than child
#    widgets.
#
#    \i It's easy to detect overlapping items (collision detection).
#
#    \i The canvas can be larger than a widget. A million-by-million canvas
#    is perfectly possible. At such a size a widget might be very
#    inefficient, and some window systems might not support it at all,
#    whereas QtCanvas scales well. Even with a billion pixels and a million
#    items, finding a particular canvas item, detecting collisions, etc.,
#    is still fast (though the memory consumption may be prohibitive
#    at such extremes).
#
#    \i Two or more QtCanvasView objects can view the same canvas.
#
#    \i An arbitrary transformation matrix can be set on each QtCanvasView
#    which makes it easy to zoom, rotate or shear the viewed canvas.
#
#    \i Widgets provide a lot more functionality, such as input (QKeyEvent,
#    QMouseEvent etc.) and layout management (QGridLayout etc.).
#
#    \endlist
#
#    A canvas consists of a background, a number of canvas items organized by
#    x, y and z coordinates, and a foreground. A canvas item's z coordinate
#    can be treated as a layer number -- canvas items with a higher z
#    coordinate appear in front of canvas items with a lower z coordinate.
#
#    The background is white by default, but can be set to a different color
#    using setBackgroundColor(), or to a repeated pixmap using
#    setBackgroundPixmap() or to a mosaic of smaller pixmaps using
#    setTiles(). Individual tiles can be set with setTile(). There
#    are corresponding get functions, e.g. backgroundColor() and
#    backgroundPixmap().
#
#    Note that QtCanvas does not inherit from QWidget, even though it has some
#    functions which provide the same functionality as those in QWidget. One
#    of these is setBackgroundPixmap(); some others are resize(), size(),
#    width() and height(). \l QtCanvasView is the widget used to display a
#    canvas on the screen.
#
#    Canvas items are added to a canvas by constructing them and passing the
#    canvas to the canvas item's constructor. An item can be moved to a
#    different canvas using QtCanvasItem.setCanvas().
#
#    Canvas items are movable (and in the case of QtCanvasSprites, animated)
#    objects that inherit QtCanvasItem. Each canvas item has a position on the
#    canvas (x, y coordinates) and a height (z coordinate), all of which are
#    held as floating-point numbers. Moving canvas items also have x and y
#    velocities. It's possible for a canvas item to be outside the canvas
#    (for example QtCanvasItem.x() is greater than width()). When a canvas
#    item is off the canvas, onCanvas() returns False and the canvas
#    disregards the item. (Canvas items off the canvas do not slow down any
#    of the common operations on the canvas.)
#
#    Canvas items can be moved with QtCanvasItem.move(). The advance()
#    function moves all QtCanvasItem.animated() canvas items and
#    setAdvancePeriod() makes QtCanvas move them automatically on a periodic
#    basis. In the context of the QtCanvas classes, to `animate' a canvas item
#    is to set it in motion, i.e. using QtCanvasItem.setVelocity(). Animation
#    of a canvas item itself, i.e. items which change over time, is enabled
#    by calling QtCanvasSprite.setFrameAnimation(), or more generally by
#    subclassing and reimplementing QtCanvasItem.advance(). To detect collisions
#    use one of the QtCanvasItem.collisions() functions.
#
#    The changed parts of the canvas are redrawn (if they are visible in a
#    canvas view) whenever update() is called. You can either call update()
#    manually after having changed the contents of the canvas, or force
#    periodic updates using setUpdatePeriod(). If you have moving objects on
#    the canvas, you must call advance() every time the objects should
#    move one step further. Periodic calls to advance() can be forced using
#    setAdvancePeriod(). The advance() function will call
#    QtCanvasItem.advance() on every item that is \link
#    QtCanvasItem.animated() animated\endlink and trigger an update of the
#    affected areas afterwards. (A canvas item that is `animated' is simply
#    a canvas item that is in motion.)
#
#    QtCanvas organizes its canvas items into \e chunks; these are areas on
#    the canvas that are used to speed up most operations. Many operations
#    start by eliminating most chunks (i.e. those which haven't changed)
#    and then process only the canvas items that are in the few interesting
#    (i.e. changed) chunks. A valid chunk, validChunk(), is one which is on
#    the canvas.
#
#    The chunk size is a key factor to QtCanvas's speed: if there are too many
#    chunks, the speed benefit of grouping canvas items into chunks is
#    reduced. If the chunks are too large, it takes too long to process each
#    one. The QtCanvas constructor tries to pick a suitable size, but you
#    can call retune() to change it at any time. The chunkSize() function
#    returns the current chunk size. The canvas items always make sure
#    they're in the right chunks; all you need to make sure of is that
#    the canvas uses the right chunk size. A good rule of thumb is that
#    the size should be a bit smaller than the average canvas item
#    size. If you have moving objects, the chunk size should be a bit
#    smaller than the average size of the moving items.
#
#    The foreground is normally nothing, but if you reimplement
#    drawForeground(), you can draw things in front of all the canvas
#    items.
#
#    Areas can be set as changed with setChanged() and set unchanged with
#    setUnchanged(). The entire canvas can be set as changed with
#    setAllChanged(). A list of all the items on the canvas is returned by
#    allItems().
#
#    An area can be copied (painted) to a QPainter with drawArea().
#
#    If the canvas is resized it emits the resized() signal.
#
#    The examples/canvas application and the 2D graphics page of the
#    examples/demo application demonstrate many of QtCanvas's facilities.
#
#    \sa QtCanvasView QtCanvasItem
###
class QtCanvas(QObject):
    resized = pyqtSignal()
    ###
    #    Create a QtCanvas with no size. \a parent is passed to the QObject
    #    superclass.
    #
    #    \warning You \e must call resize() at some time after creation to
    #    be able to use the canvas.
    ###
    def __init__(self, parent=None, *arg):
        self.pm = QPixmap()
        l = len(arg)
        if l==0:
            super(QtCanvas, self).__init__(parent)
            self.init(0, 0)
        #Constructs a QtCanvas that is \a w pixels wide and \a h pixels high.
        elif l==1:
            super(QtCanvas, self).__init__()
            self.init(parent, arg[0])
        ##
        #    Constructs a QtCanvas which will be composed of \a h tiles
        #    horizontally and \a v tiles vertically. Each tile will be an image
        #    \a tilewidth by \a tileheight pixels taken from pixmap \a p.

        #    The pixmap \a p is a list of tiles, arranged left to right, (and
        #    in the case of pixmaps that have multiple rows of tiles, top to
        #    bottom), with tile 0 in the top-left corner, tile 1 next to the
        #    right, and so on, e.g.

        #    \table
        #    \row \i 0 \i 1 \i 2 \i 3
        #    \row \i 4 \i 5 \i 6 \i 7
        #    \endtable

        #    The QtCanvas is initially sized to show exactly the given number of
        #    tiles horizontally and vertically. If it is resized to be larger,
        #    the entire matrix of tiles will be repeated as often as necessary
        #    to cover the area. If it is smaller, tiles to the right and bottom
        #    will not be visible.

        #    \sa setTiles()
        ##
        elif l==4:
            super(QtCanvas, self).__init__()
            self.init(arg[0]*arg[2], arg[1]*arg[3], scm(arg[2], arg[3]))
            self.setTiles(parent, arg[0], arg[1], arg[2], arg[3])

    def init(self, w, h, chunksze=16, mxclusters=100):
        self.d = QtCanvasData()
        self.awidth = w
        self.aheight = h
        self.chunksize = chunksze
        self.maxclusters = mxclusters
        self.chwidth = int((w+self.chunksize-1)/self.chunksize)
        self.chheight = int((h+self.chunksize-1)/self.chunksize)
        self.chunks = QList()
        for i in range(self.chwidth*self.chheight):
            self.chunks.append(QtCanvasChunk())
        self.update_timer = 0
        self.bgcolor = Qt.white
        self.grid = 0
        self.htiles = 0
        self.vtiles = 0
        self.debug_redraw_areas = False

    def tile(self, x, y):
        return self.grid[x+y*self.htiles]

    def tilesHorizontally(self):
        return self.htiles

    def tilesVertically(self):
        return self.vtiles

    def tileWidth(self):
        return self.tilew

    def tileHeight(self):
        return self.tileh

    def width(self):
        return self.awidth

    def height(self):
        return self.aheight

    def size(self):
        return QSize(self.awidth, self.aheight)

    def rect(self):
        return QRect(0, 0, self.awidth, self.aheight)

    def onCanvas(self, arg1, arg2=None):
        tp = type(arg1)
        if tp==QPoint:
            x = arg1.x()
            y = arg2.y()
        elif tp==int:
            x = arg1
            y = arg2
        return x>=0 and y>=0 and x<self.awidth and y<self.aheight

    def validChunk(self, arg1, arg2=None):
        tp = type(arg1)
        if tp==QPoint:
            x = arg1.x()
            y = arg2.y()
        elif tp==int:
            x = arg1
            y = arg2
        return x>=0 and y>=0 and x<self.chwidth and y<self.chheight

    def chunkSize(self):
        return self.chunksize

    def sameChunk(self, x1, y1, x2, y2):
        return self.x1/self.chunksize==x2/self.chunksize and y1/self.chunksize==y2/self.chunksize

    ###
    #    Destroys the canvas and all the canvas's canvas items.
    ###
    def __del__(self):
        for i in range(self.d.viewList.size()):
            self.d.viewList[i].viewing = 0
        all = self.allItems()
        for it in all:
            del it
        del self.chunks
        del self.grid
        del self.d

    ###
    #    Returns a list of canvas items that collide with the point \a p.
    #    The list is ordered by z coordinates, from highest z coordinate
    #    (front-most item) to lowest z coordinate (rear-most item).
    ###
    #    def collisions(self, p):
    #        return collisions(QRect(p, QSize(1, 1)))
    ###
    #    \overload
    #
    #    Returns a list of items which collide with the rectangle \a r. The
    #    list is ordered by z coordinates, from highest z coordinate
    #    (front-most item) to lowest z coordinate (rear-most item).
    ###
    def collisions(self, r, item=None, exact=None):
        tp = type(r)
        if tp in [QPoint, QRect]:
            if tp == QPoint:
                r = QRect(r, QSize(1, 1))
            i = QtCanvasRectangle(r, self)
            i.setPen(QPen(Qt.NoPen))
            i.show(); # doesn't actually show, since we destroy it
            l = QList(i.collisions(True))
            l = QList(sorted(l, key=lambda x:x.z(), reverse=True))
            self.removeItem(i)
            return l
        elif tp==QPolygonEx:
            ###
            #    \overload
            #
            #    Returns a list of canvas items which intersect with the chunks
            #    listed in \a chunklist, excluding \a item. If \a exact is True, 
            #    only those which actually \link QtCanvasItem.collidesWith()
            #    collide with\endlink \a item are returned; otherwise canvas items
            #    are included just for being in the chunks.
            #
            #    This is a utility function mainly used to implement the simpler
            #    QtCanvasItem.collisions() function.
            ###
            chunklist = r
            seen = QSet()
            result = QList()
            for i in range(chunklist.count()):
                x = chunklist[i].x()
                y = chunklist[i].y()
                if (self.validChunk(x, y)):
                    l = self.chunk(x, y).list()
                    for i in range(l.size()):
                        g = l.at(i)
                        if (g != item):
                            if (not seen.contains(g)):
                                seen.insert(g)
                                if (not exact or item.collidesWith(g)):
                                    item.collidesWith(g)
                                    result.append(g)
            return result

    ###
    #\internal
    #Returns the chunk at a chunk position \a i, \a j.
    ###
    def chunk(self, i, j):
        return self.chunks[i+self.chwidth*j]

    ###
    #\internal
    #Returns the chunk at a pixel position \a x, \a y.
    ###
    def chunkContaining(self, x, y):
        return self.chunk(x/self.chunksize, y/self.chunksize)

    ###
    #    Returns a list of all the items in the canvas.
    ###
    def allItems(self):
        return self.d.itemDict.toList()

    ###
    #    Changes the size of the canvas to have a width of \a w and a
    #    height of \a h. This is a slow operation.
    ###
    def resize(self, w, h):
        if (self.awidth == w and self.aheight == h):
            return

        hidden = QList()
        for it in self.d.itemDict:
            if (it.isVisible()):
                it.hide()
                hidden.append(it)

        nchwidth = (w+self.chunksize-1)/self.chunksize
        nchheight = (h+self.chunksize-1)/self.chunksize

        newchunks = QList()
        for i in range(nchwidth*nchheight):
            newchunks.append(QtCanvasChunk())

        # Commit the new values.
        #
        self.awidth = w
        self.aheight = h
        self.chwidth = nchwidth
        self.chheight = nchheight
        del self.chunks
        self.chunks = newchunks

        for i in range(hidden.size()):
            hidden.at(i).show()

        self.setAllChanged()

        self.resized.emit()

    ###
    #    \fn void QtCanvas.resized()
    #
    #    This signal is emitted whenever the canvas is resized. Each
    #    QtCanvasView connects to this signal to keep the scrollview's size
    #    correct.
    ###

    ###
    #    Change the efficiency tuning parameters to \a mxclusters clusters,
    #    each of size \a chunksze. This is a slow operation if there are
    #    many objects on the canvas.
    #
    #    The canvas is divided into chunks which are rectangular areas \a
    #    chunksze wide by \a chunksze high. Use a chunk size which is about
    #    the average size of the canvas items. If you choose a chunk size
    #    which is too small it will increase the amount of calculation
    #    required when drawing since each change will affect many chunks.
    #    If you choose a chunk size which is too large the amount of
    #    drawing required will increase because for each change, a lot of
    #    drawing will be required since there will be many (unchanged)
    #    canvas items which are in the same chunk as the changed canvas
    #    items.
    #
    #    Internally, a canvas uses a low-resolution "chunk matrix" to keep
    #    track of all the items in the canvas. A 64x64 chunk matrix is the
    #    default for a 1024x1024 pixel canvas, where each chunk collects
    #    canvas items in a 16x16 pixel square. This default is also
    #    affected by setTiles(). You can tune this default using this
    #    function. For example if you have a very large canvas and want to
    #    trade off speed for memory then you might set the chunk size to 32
    #    or 64.
    #
    #    The \a mxclusters argument is the number of rectangular groups of
    #    chunks that will be separately drawn. If the canvas has a large
    #    number of small, dispersed items, this should be about that
    #    number. Our testing suggests that a large number of clusters is
    #    almost always best.
    #
    ###
    def retune(self, chunksze, mxclusters=100):
        self.maxclusters = mxclusters

        if (self.chunksize!= chunksze):
            hidden = QList()
            for it in self.d.itemDict:
                if (it.isVisible()):
                    it.hide()
                    hidden.appendit

            self.chunksize = chunksze

            nchwidth = (self.awidth+self.chunksize-1)/self.chunksize
            nchheight = (self.aheight+self.chunksize-1)/self.chunksize

            newchunks = QList()
            for i in range(nchwidth*nchheight):
                newchunks.append(QtCanvasChunk())

            # Commit the new values.
            #
            self.chwidth = nchwidth
            self.chheight = nchheight
            del self.chunks
            self.chunks = newchunks

            for i in range(hidden.size()):
                hidden.at(i).show()

    ###
    #    \fn int QtCanvas.width()
    #
    #    Returns the width of the canvas, in pixels.
    ###

    ###
    #    \fn int QtCanvas.height()
    #
    #    Returns the height of the canvas, in pixels.
    ###

    ###
    #    \fn QSize QtCanvas.size()
    #
    #    Returns the size of the canvas, in pixels.
    ###

    ###
    #    \fn QRect QtCanvas.rect()
    #
    #    Returns a rectangle the size of the canvas.
    ###

    ###
    #    \fn bool QtCanvas.onCanvas(x, y)
    #
    #    Returns True if the pixel position (\a x, \a y) is on the canvas
    #    otherwise returns False.
    #
    #    \sa validChunk()
    ###

    ###
    #    \fn bool QtCanvas.onCanvas(p)
    #    \overload
    #
    #    Returns True if the pixel position \a p is on the canvas
    #    otherwise returns False.
    #
    #    \sa validChunk()
    ###

    ###
    #    \fn bool QtCanvas.validChunk(x, y)
    #
    #    Returns True if the chunk position (\a x, \a y) is on the canvas
    #    otherwise returns False.
    #
    #    \sa onCanvas()
    ###

    ###
    #  \fn bool QtCanvas.validChunk(p)
    #  \overload
    #
    #  Returns True if the chunk position \a p is on the canvas; otherwise
    #  returns False.
    #
    #  \sa onCanvas()
    ###

    ###
    #    \fn int QtCanvas.chunkSize()
    #
    #    Returns the chunk size of the canvas.
    #
    #    \sa retune()
    ###

    ###
    #\fn bool QtCanvas.sameChunk(x1, y1, x2, y2)
    #\internal
    #Tells if the points (\a x1, \a y1) and (\a x2, \a y2) are within the same chunk.
    ###

    ###
    #\internal
    #This method adds an the item \a item to the list of QtCanvasItem objects
    #in the QtCanvas. The QtCanvasItem class calls this.
    ###
    def addItem(self, item):
        self.d.itemDict.insert(item)

    ###
    #\internal
    #This method adds the item \a item to the list of QtCanvasItem objects
    #to be moved. The QtCanvasItem class calls this.
    ###
    def addAnimation(self, item):
        self.d.animDict.insert(item)

    ###
    #\internal
    #This method adds the item \a item  to the list of QtCanvasItem objects
    #which are no longer to be moved. The QtCanvasItem class calls this.
    ###
    def removeAnimation(self, item):
        self.d.animDict.remove(item)

    ###
    #\internal
    #This method removes the item \a item from the list of QtCanvasItem objects
    #in this QtCanvas. The QtCanvasItem class calls this.
    ###
    def removeItem(self, item):
        self.d.itemDict.remove(item)
        item.hide()

    ###
    #\internal
    #This method adds the view \a view to the list of QtCanvasView objects
    #viewing this QtCanvas. The QtCanvasView class calls this.
    ###
    def addView(self, view):
        self.d.viewList.append(view)
        if (self.htiles>1 or self.vtiles>1 or self.pm.isNull()):
            role = view.widget().backgroundRole()
            viewPalette = view.widget().palette()
            viewPalette.setColor(role, self.backgroundColor())
            view.widget().setPalette(viewPalette)

    ###
    #\internal
    #This method removes the view \a view from the list of QtCanvasView objects
    #viewing this QtCanvas. The QtCanvasView class calls this.
    ###
    def removeView(self, view):
        self.d.viewList.removeAll(view)

    ###
    #    Sets the canvas to call advance() every \a ms milliseconds. Any
    #    previous setting by setAdvancePeriod() or setUpdatePeriod() is
    #    overridden.
    #
    #    If \a ms is less than 0 advancing will be stopped.
    ###
    def setAdvancePeriod(self, ms):
        if (ms < 0):
            if (self.update_timer):
                self.update_timer.stop()
        else:
            if (self.update_timer):
                del self.update_timer
            self.update_timer = QTimer(self)
            self.update_timer.timeout.connect(self.advance)
            self.update_timer.start(ms)

    ###
    #    Sets the canvas to call update() every \a ms milliseconds. Any
    #    previous setting by setAdvancePeriod() or setUpdatePeriod() is
    #    overridden.
    #
    #    If \a ms is less than 0 automatic updating will be stopped.
    ###
    def setUpdatePeriod(self, ms):
        if (ms < 0):
            if (self.update_timer):
                self.update_timer.stop()
        else:
            if (self.update_timer):
                del self.update_timer
            self.update_timer = QTimer(self)
            self.update_timer.timeout.connect(self.update)
            self.update_timer.start(ms)

    ###
    #    Moves all QtCanvasItem.animated() canvas items on the canvas and
    #    refreshes all changes to all views of the canvas. (An `animated'
    #    item is an item that is in motion; see setVelocity().)
    #
    #    The advance takes place in two phases. In phase 0, the
    #    QtCanvasItem.advance() function of each QtCanvasItem.animated()
    #    canvas item is called with paramater 0. Then all these canvas
    #    items are called again, with parameter 1. In phase 0, the canvas
    #    items should not change position, merely examine other items on
    #    the canvas for which special processing is required, such as
    #    collisions between items. In phase 1, all canvas items should
    #    change positions, ignoring any other items on the canvas. This
    #    two-phase approach allows for considerations of "fairness",
    #    although no QtCanvasItem subclasses supplied with Qt do anything
    #    interesting in phase 0.
    #
    #    The canvas can be configured to call this function periodically
    #    with setAdvancePeriod().
    #
    #    \sa update()
    ###
    def advance(self):
        for i in self.d.animDict:
            if (i):
                i.advance(0)
        # we expect the dict contains the exact same items as in the
        # first pass.
        for i in self.d.animDict:
            if (i):
                i.advance(1)
        self.update()

    # Don't call this unless you know what you're doing.
    # p is in the content's co-ordinate example.
    ###
    #  \internal
    ###
    def drawViewArea(self, view, p, vr, bool):
        wm = view.worldMatrix()
        iwm = wm.inverted()[0]
        # ivr = covers all chunks in vr
        ivr = iwm.mapRect(vr)

        p.setTransform(wm)
        self.drawCanvasArea(ivr, p, False)

    ###
    #    Repaints changed areas in all views of the canvas.
    #
    #    \sa advance()
    ###
    def update(self):
        r = self.changeBounds()
        if r.isEmpty():
            r = self.changeBounds()
        for i in range(self.d.viewList.size()):
            view = self.d.viewList.at(i)
            if (not r.isEmpty()):
                tr = view.worldMatrix().mapRect(r)
                view.widget().update(tr)
        self.setUnchanged(r)

    ###
    #    Marks the whole canvas as changed.
    #    All views of the canvas will be entirely redrawn when
    #    update() is called next.
    ###
    def setAllChanged(self):
        self.setChanged(QRect(0, 0, self.width(), self.height()))

    ###
    #    Marks \a area as changed. This \a area will be redrawn in all
    #    views that are showing it when update() is called next.
    ###
    def setChanged(self, area):
        thearea = area.intersected(QRect(0, 0, self.width(), self.height()))

        mx = (thearea.x()+thearea.width()+self.chunksize)/self.chunksize
        my = (thearea.y()+thearea.height()+self.chunksize)/self.chunksize
        if (mx>self.chwidth):
            mx = self.chwidth
        if (my>self.chheight):
            my = self.chheight

        x = int(thearea.x()/self.chunksize)
        while(x < mx):
            y = int(thearea.y()/self.chunksize)
            while(y < my):
                self.chunk(x, y).change()
                y += 1
            x += 1

    ###
    #    Marks \a area as \e unchanged. The area will \e not be redrawn in
    #    the views for the next update(), unless it is marked or changed
    #    again before the next call to update().
    ###
    def setUnchanged(self, area):
        thearea = area.intersected(QRect(0, 0, self.width(), self.height()))

        mx = (thearea.x()+thearea.width()+self.chunksize)/self.chunksize
        my = (thearea.y()+thearea.height()+self.chunksize)/self.chunksize
        if (mx>self.chwidth):
            mx = self.chwidth
        if (my>self.chheight):
            my = self.chheight

        x = int(thearea.x()/self.chunksize)
        while(x < mx):
            y = int(thearea.y()/self.chunksize)
            while(y < my):
                self.chunk(x, y).takeChange()
                y += 1
            x += 1

    ###
    #  \internal
    ###
    def changeBounds(self):
        area = QRect(0, 0, self.width(), self.height())

        mx = (area.x()+area.width()+self.chunksize)/self.chunksize
        my = (area.y()+area.height()+self.chunksize)/self.chunksize
        if (mx > self.chwidth):
            mx = self.chwidth
        if (my > self.chheight):
            my = self.chheight

        result = QRect()

        x = int(area.x()/self.chunksize)
        while(x < mx):
            y = int(area.y()/self.chunksize)
            while(y < my):
                ch = self.chunk(x, y)
                if (ch.hasChanged()):
                    result |= QRect(x*self.chunksize, y*self.chunksize, self.chunksize + 1, self.chunksize + 1)
                y += 1
            x += 1

        return result

    ###
    #    Paints all canvas items that are in the area \a clip to \a
    #    painter, using double-buffering if \a dbuf is True.
    #
    #    e.g. to print the canvas to a printer:
    #    \code
    #    QPrinter pr
    #    if (pr.setup()):
    #        QPainter p(&pr)
    #        canvas.drawArea(canvas.rect(), &p)
    #    \endcode
    ###
    def drawArea(self, clip, painter, dbuf=False):
        if (painter):
            self.drawCanvasArea(clip, painter, dbuf)

    #include <QDebug>
    ###
    #  \internal
    ###
    def drawCanvasArea(self, inarea, p=0, double_buffer=True):###double_buffer###
        area = inarea.intersected(QRect(0, 0, self.width(), self.height()))

        if not p:
            return; # Nothing to do.

        lx = int(area.x()/self.chunksize)
        ly = int(area.y()/self.chunksize)
        mx = int(area.right()/self.chunksize)
        my = int(area.bottom()/self.chunksize)
        if (mx>= self.chwidth):
            mx = self.chwidth-1
        if (my>= self.chheight):
            my = self.chheight-1

        allvisible = QList()

        # Stores the region within area that need to be drawn. It is relative
        # to area.topLeft()  (so as to keep within bounds of 16-bit XRegions)
        rgn = QRegion()

        for x in range(lx, mx+1):
            for y in range(ly, my+1):
                # Only reset change if all views updating, and
                # wholy within area. (conservative:  ignore entire boundary)
                #
                # Disable this to help debugging.
                #
                if (not p):
                    if (self.chunk(x, y).takeChange()):
                        # ### should at least make bands
                        rgn |= QRegion(x*self.chunksize-area.x(), y*self.chunksize-area.y(),
                                       self.chunksize, self.chunksize)
                        allvisible += self.chunk(x, y).list()
                else:
                    allvisible += self.chunk(x, y).list()
        allvisible = QSet(allvisible)
        allvisible = QList(sorted(allvisible, key=lambda item:item.z(), reverse=True))

        self.drawBackground(p, area)
        if (not allvisible.isEmpty()):
            prev = 0
            for i in range(allvisible.size()-1, -1, -1):
                g = allvisible[i]
                if (g != prev):
                    g.draw(p)
                    prev = g

        self.drawForeground(p, area)

    ###
    #\internal
    #This method to informs the QtCanvas that a given chunk is
    #`dirty' and needs to be redrawn in the next Update.
    #
    #(\a x, \a y) is a chunk location.
    #
    #The sprite classes call this. Any new derived class of QtCanvasItem
    #must do so too. SetChangedChunkContaining can be used instead.
    ###
    def setChangedChunk(self, x, y):
        if (self.validChunk(x, y)):
            ch = self.chunk(x, y)
            ch.change()

    ###
    #\internal
    #This method to informs the QtCanvas that the chunk containing a given
    #pixel is `dirty' and needs to be redrawn in the next Update.
    #
    #(\a x, \a y) is a pixel location.
    #
    #The item classes call this. Any new derived class of QtCanvasItem must
    #do so too. SetChangedChunk can be used instead.
    ###
    def setChangedChunkContaining(self, x, y):
        if (x>= 0 and x < self.width() and y>= 0 and y < self.height()):
            chunk = self.chunkContaining(x, y)
            chunk.change()

    ###
    #\internal
    #This method adds the QtCanvasItem \a g to the list of those which need to be
    #drawn if the given chunk at location (\a x, \a y) is redrawn. Like
    #SetChangedChunk and SetChangedChunkContaining, this method marks the
    #chunk as `dirty'.
    ###
    def addItemToChunk(self, g, x, y):
        if (self.validChunk(x, y)):
            self.chunk(x, y).add(g)

    ###
    #\internal
    #This method removes the QtCanvasItem \a g from the list of those which need to
    #be drawn if the given chunk at location (\a x, \a y) is redrawn. Like
    #SetChangedChunk and SetChangedChunkContaining, this method marks the chunk
    #as `dirty'.
    ###
    def removeItemFromChunk(self, g, x, y):
        if (self.validChunk(x, y)):
            self.chunk(x, y).remove(g)

    ###
    #\internal
    #This method adds the QtCanvasItem \a g to the list of those which need to be
    #drawn if the chunk containing the given pixel (\a x, \a y) is redrawn. Like
    #SetChangedChunk and SetChangedChunkContaining, this method marks the
    #chunk as `dirty'.
    ###
    def addItemToChunkContaining(self, g, x, y):
        if (x>= 0 and x < self.width() and y>= 0 and y < self.height()):
            self.chunkContaining(x, y).add(g)

    ###
    #\internal
    #This method removes the QtCanvasItem \a g from the list of those which need to
    #be drawn if the chunk containing the given pixel (\a x, \a y) is redrawn.
    #Like SetChangedChunk and SetChangedChunkContaining, this method
    #marks the chunk as `dirty'.
    ###
    def removeItemFromChunkContaining(self, g, x, y):
        if (x>= 0 and x < self.width() and y>= 0 and y < self.height()):
            self.chunkContaining(x, y).remove(g)

    ###
    #    Returns the color set by setBackgroundColor(). By default, this is
    #    white.
    #
    #    This function is not a reimplementation of
    #    QWidget.backgroundColor() (QtCanvas is not a subclass of QWidget),
    #    but all QtCanvasViews that are viewing the canvas will set their
    #    backgrounds to this color.
    #
    #    \sa setBackgroundColor(), backgroundPixmap()
    ###
    def backgroundColor(self):
        return self.bgcolor

    ###
    #    Sets the solid background to be the color \a c.
    #
    #    \sa backgroundColor(), setBackgroundPixmap(), setTiles()
    ###
    def setBackgroundColor(self, c):
        if (self.bgcolor != c):
            self.bgcolor = c
            for i in range(self.d.viewList.size()):
                view = self.d.viewList.at(i)
                role = view.widget().backgroundRole()
                viewPalette = view.widget().palette()
                viewPalette.setColor(role, self.bgcolor)
                view.widget().setPalette(viewPalette)
            self.setAllChanged()

    ###
    #    Returns the pixmap set by setBackgroundPixmap(). By default,
    #    this is a null pixmap.
    #
    #    \sa setBackgroundPixmap(), backgroundColor()
    ###
    def backgroundPixmap(self):
        return self.pm

    ###
    #    Sets the solid background to be the pixmap \a p repeated as
    #    necessary to cover the entire canvas.
    #
    #    \sa backgroundPixmap(), setBackgroundColor(), setTiles()
    ###
    def setBackgroundPixmap(self, p):
        self.setTiles(p, 1, 1, p.width(), p.height())
        for i in range(self.d.viewList.size()):
            view = self.d.viewList.at(i)
            view.widget().update()

    ###
    #    This virtual function is called for all updates of the canvas. It
    #    renders any background graphics using the painter \a painter, in
    #    the area \a clip. If the canvas has a background pixmap or a tiled
    #    background, that graphic is used, otherwise the canvas is cleared
    #    using the background color.
    #
    #    If the graphics for an area change, you must explicitly call
    #    setChanged(QRect&) for the result to be visible when
    #    update() is next called.
    #
    #    \sa setBackgroundColor(), setBackgroundPixmap(), setTiles()
    ###
    def drawBackground(self, painter, clip):
        if (self.pm.isNull()):
            painter.fillRect(clip, self.bgcolor)
        elif (not self.grid):
            for x in range(int(clip.x()/self.pm.width()), int((clip.x()+clip.width()+self.pm.width()-1)/self.pm.width())):
                for y in range(int(clip.y()/self.pm.height()), int((clip.y()+clip.height()+self.pm.height()-1)/self.pm.height())):
                    painter.drawPixmap(x*self.pm.width(), y*self.pm.height(), self.pm)
        else:
            x1 = clip.left()/self.tilew
            x2 = clip.right()/self.tilew
            y1 = clip.top()/self.tileh
            y2 = clip.bottom()/self.tileh

            roww = self.pm.width()/self.tilew

            for j in range(y1, y2+1):
                jj = j%self.tilesVertically()
                for i in range(x1, x2+1):
                    t = self.tile(i%self.tilesHorizontally(), jj)
                    tx = t % roww
                    ty = t / roww
                    painter.drawPixmap(i*self.tilew, j*self.tileh, self.pm, tx*self.tilew, ty*self.tileh, self.tilew, self.tileh)

    ###
    #    This virtual function is called for all updates of the canvas. It
    #    renders any foreground graphics using the painter \a painter, in
    #    the area \a clip.
    #
    #    If the graphics for an area change, you must explicitly call
    #    setChanged(QRect&) for the result to be visible when
    #    update() is next called.
    #
    #    The default is to draw nothing.
    ###
    def drawForeground(self, painter, clip):
        if (self.debug_redraw_areas):
            painter.setPen(self.red)
            painter.setBrush(self.NoBrush)
            painter.drawRect(clip)

    ###
    #    Sets the QtCanvas to be composed of \a h tiles horizontally and \a
    #    v tiles vertically. Each tile will be an image \a tilewidth by \a
    #    tileheight pixels from pixmap \a p.
    #
    #    The pixmap \a p is a list of tiles, arranged left to right, (and
    #    in the case of pixmaps that have multiple rows of tiles, top to
    #    bottom), with tile 0 in the top-left corner, tile 1 next to the
    #    right, and so on, e.g.
    #
    #    \table
    #    \row \i 0 \i 1 \i 2 \i 3
    #    \row \i 4 \i 5 \i 6 \i 7
    #    \endtable
    #
    #    If the canvas is larger than the matrix of tiles, the entire
    #    matrix is repeated as necessary to cover the whole canvas. If it
    #    is smaller, tiles to the right and bottom are not visible.
    #
    #    The width and height of \a p must be a multiple of \a tilewidth
    #    and \a tileheight. If they are not the function will do nothing.
    #
    #    If you want to unset any tiling set, then just pass in a null
    #    pixmap and 0 for \a h, \a v, \a tilewidth, and
    #    \a tileheight.
    ###
    def setTiles(self, p, h, v, tilewidth, tileheight):
        if (not p.isNull() and (not tilewidth or not tileheight or p.width() % tilewidth != 0 or p.height() % tileheight != 0)):
            return

        self.htiles = h
        self.vtiles = v
        del self.grid
        self.pm = p
        if (h and v and not p.isNull()):
            self.grid = array('H')
            for i in range(h*v):
                self.grid.append(0)
            self.tilew = tilewidth
            self.tileh = tileheight
        else:
            self.grid = 0
        if (h + v > 10):
            s = scm(tilewidth, tileheight)
            if s<128:
                self.retune(s)
            else:
                self.retune(max(tilewidth, tileheight))
        self.setAllChanged()

    ###
    #    \fn int QtCanvas.tile(x, y)
    #
    #    Returns the tile at position (\a x, \a y). Initially, all tiles
    #    are 0.
    #
    #    The parameters must be within range, i.e.
    #        0 \< \a x \< tilesHorizontally() and
    #        0 \< \a y \< tilesVertically().
    #
    #    \sa setTile()
    ###

    ###
    #    \fn int QtCanvas.tilesHorizontally()
    #
    #    Returns the number of tiles horizontally.
    ###

    ###
    #    \fn int QtCanvas.tilesVertically()
    #
    #    Returns the number of tiles vertically.
    ###

    ###
    #    \fn int QtCanvas.tileWidth()
    #
    #    Returns the width of each tile.
    ###

    ###
    #    \fn int QtCanvas.tileHeight()
    #
    #    Returns the height of each tile.
    ###

    ###
    #    Sets the tile at (\a x, \a y) to use tile number \a tilenum, which
    #    is an index into the tile pixmaps. The canvas will update
    #    appropriately when update() is next called.
    #
    #    The images are taken from the pixmap set by setTiles() and are
    #    arranged left to right, (and in the case of pixmaps that have
    #    multiple rows of tiles, top to bottom), with tile 0 in the
    #    top-left corner, tile 1 next to the right, and so on, e.g.
    #
    #    \table
    #    \row \i 0 \i 1 \i 2 \i 3
    #    \row \i 4 \i 5 \i 6 \i 7
    #    \endtable
    #
    #    \sa tile() setTiles()
    ###
    def setTile(self, x, y, tilenum):
        t = self.grid[x+y*self.htiles]
        if (t != tilenum):
            t = tilenum
            if (self.tilew == self.tileh and self.tilew == self.chunksize):
                self.setChangedChunk(x, y);          # common case
            else:
                self.setChanged(QRect(x*self.tilew, y*self.tileh, self.tilew, self.tileh))

# lesser-used data in canvas item, plus room for extension.
# Be careful adding to this - check all usages.
class QtCanvasItemExtra():
    def __init__(self):
        self.vx = 0.0
        self.vy = 0.0

###
#    \class QtCanvasItem qtcanvas.h
#    \brief The QtCanvasItem class provides an abstract graphic object on a QtCanvas.
#
#    A variety of QtCanvasItem subclasses provide immediately usable
#    behaviour. This class is a pure abstract superclass providing the
#    behaviour that is shared among all the concrete canvas item classes.
#    QtCanvasItem is not intended for direct subclassing. It is much easier
#    to subclass one of its subclasses, e.g. QtCanvasPolygonalItem (the
#    commonest base class), QtCanvasRectangle, QtCanvasSprite, QtCanvasEllipse
#    or QtCanvasText.
#
#    Canvas items are added to a canvas by constructing them and passing the
#    canvas to the canvas item's constructor. An item can be moved to a
#    different canvas using setCanvas().
#
#    Items appear on the canvas after their \link show() show()\endlink
#    function has been called (or \link setVisible()
#    setVisible(True)\endlink), and \e after update() has been called. The
#    canvas only shows items that are \link setVisible() visible\endlink,
#    and then only if \l update() is called. If you created the canvas
#    without passing a width and height to the constructor you'll also need
#    to call \link QtCanvas.resize() resize()\endlink. Since the canvas
#    background defaults to white and canvas items default to white,
#    you may need to change colors to see your items.
#
#    A QtCanvasItem object can be moved in the x(), y() and z() dimensions
#    using functions such as move(), moveBy(), setX(), setY() and setZ(). A
#    canvas item can be set in motion, `animated', using setAnimated() and
#    given a velocity in the x and y directions with setXVelocity() and
#    setYVelocity() -- the same effect can be achieved by calling
#    setVelocity(). Use the collidesWith() function to see if the canvas item
#    will collide on the \e next advance(1) and use collisions() to see what
#    collisions have occurred.
#
#    Use QtCanvasSprite or your own subclass of QtCanvasSprite to create canvas
#    items which are animated, i.e. which change over time.
#
#    The size of a canvas item is given by boundingRect(). Use
#    boundingRectAdvanced() to see what the size of the canvas item will be
#    \e after the next advance(1) call.
#
#    The rtti() function is used for identifying subclasses of QtCanvasItem.
#    The canvas() function returns a pointer to the canvas which contains the
#    canvas item.
#
#    QtCanvasItem provides the show() and isVisible() functions like those in
#    QWidget.
#
#    QtCanvasItem also provides the setEnabled(), setActive() and
#    setSelected() functions; these functions set the relevant boolean and
#    cause a repaint but the boolean values they set are not used in
#    QtCanvasItem itself. You can make use of these booleans in your subclasses.
#
#    By default, canvas items have no velocity, no size, and are not in
#    motion. The subclasses provided in Qt do not change these defaults
#    except where noted.
#
###
class QtCanvasItem():
    ###
    #    Constructs a QtCanvasItem on canvas \a canvas.
    #
    #    \sa setCanvas()
    ###
    def __init__(self, canvas):
        self.cnv = canvas
        self.myx = 0.0
        self.myy = 0.0
        self.myz = 0.0
        self.ani = 0
        self.vis = 0
        self.val = 0
        self.sel = 0
        self.ena = 0
        self.act = 0

        self.ext = 0
        if (self.cnv):
            self.cnv.addItem(self)

    def isNone(self):
        return self.cnv==None

    ###
    #    Destroys the QtCanvasItem and removes it from its canvas.
    ###
    def __del__(self):
        if (self.cnv):
            self.cnv.removeItem(self)
            self.cnv.removeAnimation(self)
        del self.ext

    ###
    #    Returns the list of canvas items that this canvas item has
    #    collided with.
    #
    #    A collision is generally defined as occurring when the pixels of
    #    one item draw on the pixels of another item, but not all
    #    subclasses are so precise. Also, since pixel-wise collision
    #    detection can be slow, this function works in either exact or
    #    inexact mode, according to the \a exact parameter.
    #
    #    If \a exact is True, the canvas items returned have been
    #    accurately tested for collision with the canvas item.
    #
    #    If \a exact is False, the canvas items returned are \e near the
    #    canvas item. You can test the canvas items returned using
    #    collidesWith() if any are interesting collision candidates. By
    #    using this approach, you can ignore some canvas items for which
    #    collisions are not relevant.
    #
    #    The returned list is a list of QtCanvasItems, but often you will
    #    need to cast the items to their subclass types. The safe way to do
    #    this is to use rtti() before casting. This provides some of the
    #    functionality of the standard C++ dynamic cast operation even on
    #    compilers where dynamic casts are not available.
    #
    #    Note that a canvas item may be `on' a canvas, e.g. it was created
    #    with the canvas as parameter, even though its coordinates place it
    #    beyond the edge of the canvas's area. Collision detection only
    #    works for canvas items which are wholly or partly within the
    #    canvas's area.
    #
    #    Note that if items have a velocity (see \l setVelocity()), then
    #    collision testing is done based on where the item \e will be when
    #    it moves, not its current location. For example, a "ball" item
    #    doesn't need to actually embed into a "wall" item before a
    #    collision is detected. For items without velocity, plain
    #    intersection is used.
    ###
    def collisions(self, exact):
        return self.canvas().collisions(self.chunks(), self, exact)

    ###
    #    Returns 0 (RttiValues.Rtti_Item).
    #
    #    Make your derived classes return their own values for rtti(), so
    #    that you can distinguish between objects returned by
    #    QtCanvas.at(). You should use values greater than 1000 to allow
    #    for extensions to this class.
    #
    #    Overuse of this functionality can damage its extensibility. For
    #    example, once you have identified a base class of a QtCanvasItem
    #    found by QtCanvas.at(), cast it to that type and call meaningful
    #    methods rather than acting upon the object based on its rtti
    #    value.
    #
    #    For example:
    #
    #    \code
    #        item
    #        # Find an item, e.g. with QtCanvasItem.collisions().
    #        ...
    #        if (item.rtti() == MySprite.RTTI):
    #            s = (MySprite*)item
    #            if (s.isDamagable()) s.loseHitPoints(1000):
    #            if (s.isHot()) myself.loseHitPoints(1000):
    #            ...
    #    \endcode
    ###
    def rtti(self):
        return self.RTTI

    RTTI = RttiValues.Rtti_Item
    def extra(self):
        if (not self.ext):
            self.ext = QtCanvasItemExtra
        return self.ext

    ###
    #    \fn double QtCanvasItem.x()
    #
    #    Returns the horizontal position of the canvas item. Note that
    #    subclasses often have an origin other than the top-left corner.
    ###
    def x(self):
        return self.myx
    ###
    #    \fn double QtCanvasItem.y()
    #
    #    Returns the vertical position of the canvas item. Note that
    #    subclasses often have an origin other than the top-left corner.
    ###
    def y(self):
        return self.myy
    ###
    #    \fn double QtCanvasItem.z()
    #
    #    Returns the z index of the canvas item, which is used for visual
    #    order: higher-z items obscure (are in front of) lower-z items.
    ###
    def z(self):
        return self.myz
    ###
    #    \fn void QtCanvasItem.setX(double x)
    #
    #    Moves the canvas item so that its x-position is \a x.
    #
    #    \sa x(), move()
    ###
    def setX(self, a):
        self.move(a,self.y())
    ###
    #    \fn void QtCanvasItem.setY(double y)
    #
    #    Moves the canvas item so that its y-position is \a y.
    #
    #    \sa y(), move()
    ###
    def setY(self, a):
        self.move(self.x(), a)
    ###
    #    \fn void QtCanvasItem.setZ(double z)
    #
    #    Sets the z index of the canvas item to \a z. Higher-z items
    #    obscure (are in front of) lower-z items.
    #
    #    \sa z(), move()
    ###
    def setZ(self, a):
        self.myz=a
        self.changeChunks()
    ###
    #    Moves the canvas item relative to its current position by (\a dx,
    #    \a dy).
    ###
    def moveBy(self, dx, dy):
        if (dx or dy):
            self.removeFromChunks()
            self.myx += dx
            self.myy += dy
            self.addToChunks()

    ###
    #    Moves the canvas item to the absolute position (\a x, \a y).
    ###
    def move(self, x, y):
        self.moveBy(x-self.myx, y-self.myy)

    ###
    #  \internal
    #  Removes the item from all the chunks it covers.
    ###
    def removeFromChunks(self):
        if (self.isVisible() and self.canvas()):
            pa = QPolygonEx(self.chunks())
            for i in range(pa.count()):
                self.canvas().removeItemFromChunk(self, pa[i].x(), pa[i].y())

    ###
    #    Returns True if the canvas item is in motion; otherwise returns
    #    False.
    #
    #    \sa setVelocity(), setAnimated()
    ###
    def animated(self):
        return self.ani

    ###
    #    Sets the canvas item to be in motion if \a y is True, or not if \a
    #    y is False. The speed and direction of the motion is set with
    #    setVelocity(), or with setXVelocity() and setYVelocity().
    #
    #    \sa advance(), QtCanvas.advance()
    ###
    def setAnimated(self, y):
        if (y != self.ani):
            self.ani = y
            if (y):
                self.cnv.addAnimation(self)
            else:
                self.cnv.removeAnimation(self)

    ###
    #    \fn void QtCanvasItem.setXVelocity(double vx)
    #
    #    Sets the horizontal component of the canvas item's velocity to \a vx.
    #
    #    \sa setYVelocity() setVelocity()
    ###
    def setXVelocity(self, vx):
        self.setVelocity(vx, self.yVelocity())
    ###
    #    \fn void QtCanvasItem.setYVelocity(double vy)
    #
    #    Sets the vertical component of the canvas item's velocity to \a vy.
    #
    #    \sa setXVelocity() setVelocity()
    ###
    def setYVelocity(self, vy):
        self.setVelocity(self.xVelocity(), vy)
    ###
    #    Sets the canvas item to be in motion, moving by \a vx and \a vy
    #    pixels in the horizontal and vertical directions respectively.
    #
    #    \sa advance() setXVelocity() setYVelocity()
    ###
    def setVelocity(self, vx, vy):
        if (self.ext or vx!= 0.0 or vy!= 0.0):
            if (not self.ani):
                self.setAnimated(True)
            self.extra().vx = vx
            self.extra().vy = vy

    ###
    #    Returns the horizontal velocity component of the canvas item.
    ###
    def xVelocity(self):
        if self.ext:
            return self.ext.vx
        return 0

    ###
    #    Returns the vertical velocity component of the canvas item.
    ###
    def yVelocity(self):
        if self.ext:
            return self.ext.vy
        return 0

    ###
    #    The default implementation moves the canvas item, if it is
    #    animated(), by the preset velocity if \a phase is 1, and does
    #    nothing if \a phase is 0.
    #
    #    Note that if you reimplement this function, the reimplementation
    #    must not change the canvas in any way, for example it must not add
    #    or remove items.
    #
    #    \sa QtCanvas.advance() setVelocity()
    ###
    def advance(self, phase):
        if (self.ext and phase == 1):
            self.moveBy(self.ext.vx, self.ext.vy)

    ###
    #    \fn void QtCanvasItem.draw(painter)
    #
    #    This abstract virtual function draws the canvas item using \a painter.
    ###

    ###
    #    Sets the QtCanvas upon which the canvas item is to be drawn to \a c.
    #
    #    \sa canvas()
    ###
    def setCanvas(self, c):
        v = self.isVisible()
        self.setVisible(False)
        if (self.cnv):
            if (self.ext):
                self.cnv.removeAnimation(self)
            self.cnv.removeItem(self)
        self.cnv = c
        if (self.cnv):
            self.cnv.addItem(self)
            if (self.ext):
                self.cnv.addAnimation(self)
        self.setVisible(v)

    ###
    #    \fn QtCanvasItem.canvas()
    #
    #    Returns the canvas containing the canvas item.
    ###
    def canvas(self):
        return self.cnv

    ###
    #  \internal
    #  Returns the chunks covered by the item.
    ###
    def chunks(self):
        r = QPolygonEx()
        n = 0
        br = self.boundingRect()
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            br &= QRect(0, 0, self.canvas().width(), self.canvas().height())
            if (br.isValid()):
                r.resize(int(br.width()/self.chunksize+2)*int(br.height()/self.chunksize+2))
                for j in range(int(br.top()/self.chunksize), int(br.bottom()/self.chunksize+1)):
                    for i in range(int(br.left()/self.chunksize), int(br.right()/self.chunksize+1)):
                        r[n] = QPoint(i, j)
                        n += 1
        r.resize(n)
        return r

    ### Shorthand for setVisible(True). ###
    def show(self):
        self.setVisible(True)

    ### Shorthand for setVisible(False). ###
    def hide(self):
        self.setVisible(False)

    ###
    #    Makes the canvas item visible if \a yes is True, or invisible if
    #    \a yes is False. The change takes effect when QtCanvas.update() is
    #    next called.
    ###
    def setVisible(self, yes):
        if (self.vis != yes):
            if (yes):
                self.vis = yes
                self.addToChunks()
            else:
                self.removeFromChunks()
                self.vis = yes

    ###
    #    \obsolete
    #    \fn bool QtCanvasItem.visible()
    #    Use isVisible() instead.
    ###
    def visible(self):
        return self.vis

    ###
    #    \fn bool QtCanvasItem.isVisible()
    #
    #    Returns True if the canvas item is visible; otherwise returns
    #    False.
    #
    #    Note that in this context True does \e not mean that the canvas
    #    item is currently in a view, merely that if a view is showing the
    #    area where the canvas item is positioned, and the item is not
    #    obscured by items with higher z values, and the view is not
    #    obscured by overlaying windows, it would be visible.
    #
    #    \sa setVisible(), z()
    ###
    def isVisible(self):
        return self.vis

    ###
    #    \obsolete
    #    \fn bool QtCanvasItem.selected()
    #    Use isSelected() instead.
    ###
    def selected(self):
        return self.sel

    ###
    #    \fn bool QtCanvasItem.isSelected()
    #
    #    Returns True if the canvas item is selected; otherwise returns False.
    ###
    def isSelected(self):
        return self.sel

    ###
    #    Sets the selected flag of the item to \a yes. If this changes the
    #    item's selected state the item will be redrawn when
    #    QtCanvas.update() is next called.
    #
    #    The QtCanvas, QtCanvasItem and the Qt-supplied QtCanvasItem
    #    subclasses do not make use of this value. The setSelected()
    #    function is supplied because many applications need it, but it is
    #    up to you how you use the isSelected() value.
    ###
    def setSelected(self, yes):
        if (self.sel != yes):
            self.sel = yes
            self.changeChunks()

    ###
    #    \obsolete
    #    \fn bool QtCanvasItem.enabled()
    #    Use isEnabled() instead.
    ###
    def enabled(self):
        return self.ena

    ###
    #    \fn bool QtCanvasItem.isEnabled()
    #
    #    Returns True if the QtCanvasItem is enabled; otherwise returns False.
    ###
    def isEnabled(self):
        return self.ena

    ###
    #    Sets the enabled flag of the item to \a yes. If this changes the
    #    item's enabled state the item will be redrawn when
    #    QtCanvas.update() is next called.
    #
    #    The QtCanvas, QtCanvasItem and the Qt-supplied QtCanvasItem
    #    subclasses do not make use of this value. The setEnabled()
    #    function is supplied because many applications need it, but it is
    #    up to you how you use the isEnabled() value.
    ###
    def setEnabled(self, yes):
        if (self.ena!= yes):
            self.ena = yes
            self.changeChunks()

    ###
    #    \obsolete
    #    \fn bool QtCanvasItem.active()
    #    Use isActive() instead.
    ###
    def active(self):
        return self.act

    ###
    #    \fn bool QtCanvasItem.isActive()
    #
    #    Returns True if the QtCanvasItem is active; otherwise returns False.
    ###
    def isActive(self):
        return self.act

    ###
    #    Sets the active flag of the item to \a yes. If this changes the
    #    item's active state the item will be redrawn when
    #    QtCanvas.update() is next called.
    #
    #    The QtCanvas, QtCanvasItem and the Qt-supplied QtCanvasItem
    #    subclasses do not make use of this value. The setActive() function
    #    is supplied because many applications need it, but it is up to you
    #    how you use the isActive() value.
    ###
    def setActive(self, yes):
        if (self.act!= yes):
            self.act = yes
            self.changeChunks()

    ###
    #    \fn void QtCanvasItem.update()
    #
    #    Call this function to repaint the canvas's changed chunks.
    ###
    def update(self):
        self.changeChunks()

    ###
    #    \class QtCanvasSprite qtcanvas.h
    #    \brief The QtCanvasSprite class provides an animated canvas item on a QtCanvas.
    #
    #    A canvas sprite is an object which can contain any number of images
    #    (referred to as frames), only one of which is current, i.e.
    #    displayed, at any one time. The images can be passed in the
    #    constructor or set or changed later with setSequence(). If you
    #    subclass QtCanvasSprite you can change the frame that is displayed
    #    periodically, e.g. whenever QtCanvasItem.advance(1) is called to
    #    create the effect of animation.
    #
    #    The current frame can be set with setFrame() or with move(). The
    #    number of frames available is given by frameCount(). The bounding
    #    rectangle of the current frame is returned by boundingRect().
    #
    #    The current frame's image can be retrieved with image(); use
    #    imageAdvanced() to retrieve the image for the frame that will be
    #    shown after advance(1) is called. Use the image() overload passing
    #    it an integer index to retrieve a particular image from the list of
    #    frames.
    #
    #    Use width() and height() to retrieve the dimensions of the current
    #    frame.
    #
    #    Use leftEdge() and rightEdge() to retrieve the current frame's
    #    left-hand and right-hand x-coordinates respectively. Use
    #    bottomEdge() and topEdge() to retrieve the current frame's bottom
    #    and top y-coordinates respectively. These functions have an overload
    #    which will accept an integer frame number to retrieve the
    #    coordinates of a particular frame.
    #
    #    QtCanvasSprite draws very quickly, at the expense of memory.
    #
    #    The current frame's image can be drawn on a painter with draw().
    #
    #    Like any other canvas item, canvas sprites can be moved with
    #    move() which sets the x and y coordinates and the frame number, as
    #    well as with QtCanvasItem.move() and QtCanvasItem.moveBy(), or by
    #    setting coordinates with QtCanvasItem.setX(), QtCanvasItem.setY()
    #    and QtCanvasItem.setZ().
    #
    ###

    ###
    #  \internal
    #  Adds the item to all the chunks it covers.
    ###
    def addToChunks(self):
        if (self.isVisible() and self.canvas()):
            pa = self.chunks()
            for i in range(pa.count()):
                self.canvas().addItemToChunk(self, pa[i].x(), pa[i].y())
            self.val = True

    ###
    #  \internal
    #  Sets all the chunks covered by the item to be refreshed with QtCanvas.update()
    #  is next called.
    ###
    def changeChunks(self):
        if (self.isVisible() and self.canvas()):
            if (not self.val):
                self.addToChunks()
            pa = QPolygonEx(self.chunks())
            for i in range(pa.count()):
                self.canvas().setChangedChunk(pa[i].x(), pa[i].y())

    ###
    #    \fn QRect QtCanvasItem.boundingRect()
    #
    #    Returns the bounding rectangle in pixels that the canvas item covers.
    #
    #    \sa boundingRectAdvanced()
    ###

    ###
    #    Returns the bounding rectangle of pixels that the canvas item \e
    #    will cover after advance(1) is called.
    #
    #    \sa boundingRect()
    ###
    def boundingRectAdvanced(self):
        dx = int(self.x()+self.xVelocity())-int(self.x())
        dy = int(self.y()+self.yVelocity())-int(self.y())
        r = self.boundingRect()
        r.translate(dx, dy)
        return r

    ###
    #    \class QtCanvasPixmap qtcanvas.h
    #    \brief The QtCanvasPixmap class provides pixmaps for QtCanvasSprites.
    #
    #    If you want to show a single pixmap on a QtCanvas use a
    #    QtCanvasSprite with just one pixmap.
    #
    #    When pixmaps are inserted into a QtCanvasPixmapArray they are held
    #    as QtCanvasPixmaps. \l{QtCanvasSprite}s are used to show pixmaps on
    #    \l{QtCanvas}es and hold their pixmaps in a QtCanvasPixmapArray. If
    #    you retrieve a frame (pixmap) from a QtCanvasSprite it will be
    #    returned as a QtCanvasPixmap.
    #
    #    The pixmap is a QPixmap and can only be set in the constructor.
    #    There are three different constructors, one taking a QPixmap, one
    #    a QImage and one a file name that refers to a file in any
    #    supported file format (see QImageReader).
    #
    #    QtCanvasPixmap can have a hotspot which is defined in terms of an (x,
    #    y) offset. When you create a QtCanvasPixmap from a PNG file or from
    #    a QImage that has a QImage.offset(), the offset() is initialized
    #    appropriately, otherwise the constructor leaves it at (0, 0). You
    #    can set it later using setOffset(). When the QtCanvasPixmap is used
    #    in a QtCanvasSprite, the offset position is the point at
    #    QtCanvasItem.x() and QtCanvasItem.y(), not the top-left corner of
    #    the pixmap.
    #
    #    Note that for QtCanvasPixmap objects created by a QtCanvasSprite, the
    #    position of each QtCanvasPixmap object is set so that the hotspot
    #    stays in the same position.
    #
    #    \sa QtCanvasPixmapArray QtCanvasItem QtCanvasSprite
    ###

class QtCanvasPixmap(QPixmap):
    def __init__(self, image, offset=None):
        self.hotx = 0
        self.hoty = 0
        self.collision_mask = None

        if not offset:
            ###
            #    Constructs a QtCanvasPixmap from the pixmap \a pm using the offset
            #    \a offset.
            ###
            self.init(self.pm, offset.x(), offset.y())
        else:
            if type(image)==str:
                ###
                #    Constructs a QtCanvasPixmap that uses the image stored in \a
                #    datafilename.
                ###
                image = QImage(image)
            ###
            #    Constructs a QtCanvasPixmap from the image \a image.
            ###
            self.init(image)

    def offsetX(self):
        return self.hotx

    def offsetY(self):
        return self.hoty

    def setOffset(self, x, y):
        self.hotx = x
        self.hoty = y

    def init(self, pixmap, hx=None, hy=None):
        t = type(pixmap)
        if t==QImage:
            image = pixmap
            self.QPixmap.operator = QPixmap.fromImage(image)
            self.hotx = image.offset().x()
            self.hoty = image.offset().y()
    #ifndef QT_NO_IMAGE_DITHER_TO_1
            if(image.hasAlphaChannel()):
                i = image.createAlphaMask()
                self.collision_mask = QImage(i)
            else:
    #endif
                self.collision_mask = 0
        elif t==QPixmap:
            self = pixmap
            self.hotx = hx
            self.hoty = hy
            if(pixmap.hasAlphaChannel()):
                i = self.mask().toImage()
                self.collision_mask = QImage(i)
            else:
                self.collision_mask = 0

    ###
    #    Destroys the pixmap.
    ###
    def __del__(self):
        del self.collision_mask

    ###
    #    \fn int QtCanvasPixmap.offsetX()
    #
    #    Returns the x-offset of the pixmap's hotspot.
    #
    #    \sa setOffset()
    ###

    ###
    #    \fn int QtCanvasPixmap.offsetY()
    #
    #    Returns the y-offset of the pixmap's hotspot.
    #
    #    \sa setOffset()
    ###

    ###
    #    \fn void QtCanvasPixmap.setOffset(x, y)
    #
    #    Sets the offset of the pixmap's hotspot to (\a x, \a y).
    #
    #    \warning Do not call this function if any QtCanvasSprites are
    #    currently showing this pixmap.
    ###

    ###
    #    \class QtCanvasPixmapArray qtcanvas.h
    #    \brief The QtCanvasPixmapArray class provides an array of QtCanvasPixmaps.
    #
    #    This class is used by QtCanvasSprite to hold an array of pixmaps.
    #    It is used to implement animated sprites, i.e. images that change
    #    over time, with each pixmap in the array holding one frame.
    #
    #    Depending on the constructor you use you can load multiple pixmaps
    #    into the array either from a directory (specifying a wildcard
    #    pattern for the files), or from a list of QPixmaps. You can also
    #    read in a set of pixmaps after construction using readPixmaps().
    #
    #    Individual pixmaps can be set with setImage() and retrieved with
    #    image(). The number of pixmaps in the array is returned by
    #    count().
    #
    #    QtCanvasSprite uses an image's mask for collision detection. You
    #    can change this by reading in a separate set of image masks using
    #    readCollisionMasks().
    #
    ###

    ###
    #    Constructs an invalid array (i.e. isValid() will return False).
    #    You must call readPixmaps() before being able to use this
    #    QtCanvasPixmapArray.
    ###
class QtCanvasPixmapArray():
    def __init__(self, arg1=None, arg2=None):
        self.framecount = 0
        self.img = 0
        t1 = type(arg1)
        if t1 == str:
            ###
            #    Constructs a QtCanvasPixmapArray from files.
            #
            #    The \a fc parameter sets the number of frames to be loaded for
            #    this image.
            #
            #    If \a fc is not 0, \a datafilenamepattern should contain "%1", 
            #    e.g. "foo%1.png". The actual filenames are formed by replacing the
            #    %1 with four-digit integers from 0 to (fc - 1), e.g. foo0000.png,
            #    foo0001.png, foo0002.png, etc.
            #
            #    If \a fc is 0, \a datafilenamepattern is asssumed to be a
            #    filename, and the image contained in this file will be loaded as
            #    the first (and only) frame.
            #
            #    If \a datafilenamepattern does not exist, is not readable, isn't
            #    an image, or some other error occurs, the array ends up empty and
            #    isValid() returns False.
            ###
            datafilenamepattern = arg1
            fc = arg2
            self.readPixmaps(datafilenamepattern, fc)
        elif t1 == QList:
            ###
            #  \obsolete
            #class QtCanvasPixmapArray():(QtValueList<QPixmap>, QPolygon)
            #  instead.
            #
            #  Constructs a QtCanvasPixmapArray from the list of QPixmaps \a
            #  list. The \a hotspots list has to be of the same size as \a list.
            ###
            l = arg1
            hotspots = arg2
            self.framecount = l.count()
            self.img = QList()
            for i in range(self.framecount):
                self.img.append(0)
            if (l.count() != self.hotspots.count()):
                qWarning("QtCanvasPixmapArray: lists have different lengths")
                self.reset()
                self.img = 0
            else:
                for i in range(self.framecount):
                    self.img[i] = QtCanvasPixmap(l.at(i), hotspots.at(i))

    ###
    #    Destroys the pixmap array and all the pixmaps it contains.
    ###
    def __del__(self):
        self.reset()

    def reset(self):
        for i in range(self.framecount):
            del self.img[i]
        del self.img
        self.img = 0
        self.framecount = 0

    ###
    #    Reads one or more pixmaps into the pixmap array.
    #
    #    If \a fc is not 0, \a filenamepattern should contain "%1", e.g.
    #    "foo%1.png". The actual filenames are formed by replacing the %1
    #    with four-digit integers from 0 to (fc - 1), e.g. foo0000.png,
    #    foo0001.png, foo0002.png, etc.
    #
    #    If \a fc is 0, \a filenamepattern is asssumed to be a filename,
    #    and the image contained in this file will be loaded as the first
    #    (and only) frame.
    #
    #    If \a filenamepattern does not exist, is not readable, isn't an
    #    image, or some other error occurs, this function will return
    #    False, and isValid() will return False; otherwise this function
    #    will return True.
    #
    #    \sa isValid()
    ###
    #    def readPixmaps(self, filenamepattern, fc):
    #        return self.readPixmaps(filenamepattern, fc, False)

    ###
    #    Reads new collision masks for the array.
    #
    #    By default, QtCanvasSprite uses the image mask of a sprite to
    #    detect collisions. Use this function to set your own collision
    #    image masks.
    #
    #    If count() is 1 \a filename must specify a real filename to read
    #    the mask from. If count() is greater than 1, the \a filename must
    #    contain a "%1" that will get replaced by the number of the mask to
    #    be loaded, just like QtCanvasPixmapArray.readPixmaps().
    #
    #    All collision masks must be 1-bit images or this function call
    #    will fail.
    #
    #    If the file isn't readable, contains the wrong number of images,
    #    or there is some other error, this function will return False, and
    #    the array will be flagged as invalid; otherwise this function
    #    returns True.
    #
    #    \sa isValid()
    ###
    def readCollisionMasks(self, filename):
        return self.readPixmaps(filename, self.framecount, True)

    def readPixmaps(self, datafilenamepattern, fc, maskonly=False):
        if (not maskonly):
            self.reset()
            framecount = fc
            if (not framecount):
                framecount = 1
            img = QtCanvasPixmap[framecount]
        if (not img):
            return False

        ok = True
        arg = fc > 1
        if (not arg):
            framecount = 1
        for i in range(framecount):
            r = ''
            r.format("%04d", i)
            if (maskonly):
                if (not img[i].collision_mask):
                    img[i].collision_mask = QImage()
                if arg:
                    img[i].collision_mask.load(datafilenamepattern%r)
                else:
                    img[i].collision_mask.load(datafilenamepattern)
                ok = ok and not img[i].collision_mask.isNull() and self.img[i].collision_mask.depth() == 1
            else:
                if arg:
                    img[i] = QtCanvasPixmap(datafilenamepattern%r)
                else:
                    img[i] = QtCanvasPixmap(datafilenamepattern)
                ok = ok and not img[i].isNull()
        if (not ok):
            self.reset()
        return ok

    ###
    #  \obsolete
    #
    #  Use isValid() instead.
    #
    #  This returns False if the array is valid, and True if it is not.
    ###
    #    def operator!(self):
    #        return img == 0

    ###
    #    Returns True if the pixmap array is valid; otherwise returns
    #    False.
    ###
    def isValid(self):
        return self.img != 0

    ###
    #    \fn QtCanvasPixmapArray.image(i)
    #
    #    Returns pixmap \a i in the array, if \a i is non-negative and less
    #    than than count(), and returns an unspecified value otherwise.
    ###

    # ### wouldn't it be better to put empty QtCanvasPixmaps in there instead of
    # initializing the additional elements in the array to 0? Lars
    ###
    #    Replaces the pixmap at index \a i with pixmap \a p.
    #
    #    The array takes ownership of \a p and will delete \a p when the
    #    array itself is deleted.
    #
    #    If \a i is beyond the end of the array the array is extended to at
    #    least i+1 elements, with elements count() to i-1 being initialized
    #    to 0.
    ###
    def setImage(self, i, p):
        if (i >= self.framecount):
            for x in range(i+1-self.framecount):
                self.img.append(0)
        del self.img[i]
        self.img[i] = p

    ###
    #    \fn uint QtCanvasPixmapArray.count()
    #
    #    Returns the number of pixmaps in the array.
    ###

    ###
    #    Returns the x-coordinate of the current left edge of the sprite.
    #    (This may change as the sprite animates since different frames may
    #    have different left edges.)
    #
    #    \sa rightEdge() bottomEdge() topEdge()
    ###
    #    def leftEdge(self):
    #        return int(self.x()) - self.image().hotx

    ###
    #    \overload
    #
    #    Returns what the x-coordinate of the left edge of the sprite would
    #    be if the sprite (actually its hotspot) were moved to x-position
    #    \a nx.
    #
    #    \sa rightEdge() bottomEdge() topEdge()
    ###
    def leftEdge(self, nx=None):
        if nx is None:
            nx = self.x()
        return nx - self.image().hotx

    ###
    #    Returns the y-coordinate of the top edge of the sprite. (This may
    #    change as the sprite animates since different frames may have
    #    different top edges.)
    #
    #    \sa leftEdge() rightEdge() bottomEdge()
    ###
    #    def topEdge(self):
    #        return int(self.y()) - self.image().hoty

    ###
    #    \overload
    #
    #    Returns what the y-coordinate of the top edge of the sprite would
    #    be if the sprite (actually its hotspot) were moved to y-position
    #    \a ny.
    #
    #    \sa leftEdge() rightEdge() bottomEdge()
    ###
    def topEdge(self, ny=None):
        if ny is None:
            ny = self.y()
        return ny - self.image().hoty

    ###
    #    Returns the x-coordinate of the current right edge of the sprite.
    #    (This may change as the sprite animates since different frames may
    #    have different right edges.)
    #
    #    \sa leftEdge() bottomEdge() topEdge()
    ###
    #    def rightEdge(self):
    #        return self.leftEdge() + self.image().width()-1

    ###
    #    \overload
    #
    #    Returns what the x-coordinate of the right edge of the sprite
    #    would be if the sprite (actually its hotspot) were moved to
    #    x-position \a nx.
    #
    #    \sa leftEdge() bottomEdge() topEdge()
    ###
    def rightEdge(self, nx=None):
        if nx is None:
            x = self.leftEdge()
        else:
            x = self.leftEdge(nx)
        return x + self.image().width()-1

    ###
    #    Returns the y-coordinate of the current bottom edge of the sprite.
    #    (This may change as the sprite animates since different frames may
    #    have different bottom edges.)
    #
    #    \sa leftEdge() rightEdge() topEdge()
    ###
    #    def bottomEdge(self):
    #        return self.topEdge() + self.image().height()-1

    ###
    #    \overload
    #
    #    Returns what the y-coordinate of the top edge of the sprite would
    #    be if the sprite (actually its hotspot) were moved to y-position
    #    \a ny.
    #
    #    \sa leftEdge() rightEdge() topEdge()
    ###
    def bottomEdge(self, ny=None):
        if ny is None:
            x = self.topEdge()
        else:
            x = self.topEdge(ny)
        return x + self.image().height()-1

    ###
    #    \fn QtCanvasSprite.image()
    #
    #    Returns the current frame's image.
    #
    #    \sa frame(), setFrame()
    ###

    ###
    #    \fn QtCanvasSprite.image(f)
    #    \overload
    #
    #    Returns the image for frame \a f. Does not do any bounds checking on \a f.
    ###
    def image(self, f=None):
        x = f
        if x is None:
            x = self.frm
        return self.images.image(x)

    ###
    #    Returns the image the sprite \e will have after advance(1) is
    #    called. By default this is the same as image().
    ###
    def imageAdvanced(self):
        return self.image()

    ###
    #    Returns the bounding rectangle for the image in the sprite's
    #    current frame. This assumes that the images are tightly cropped
    #    (i.e. do not have transparent pixels all along a side).
    ###
    def boundingRect(self):
        return QRect(self.leftEdge(), self.topEdge(), self.width(), self.height())

    def canvas(self):
        return self.cnv
    ###
    #  \internal
    #  Add the sprite to the chunks in its QtCanvas which it overlaps.
    ###
    def addToChunks(self):
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            for j in range(int(self.topEdge()/self.chunksize), int(self.bottomEdge()/self.chunksize+1)):
                for i in range(int(self.leftEdge()/self.chunksize), int(self.rightEdge()/self.chunksize+1)):
                    self.canvas().addItemToChunk(self, i, j)

    ###
    #  \internal
    #  Remove the sprite from the chunks in its QtCanvas which it overlaps.
    #
    #  \sa addToChunks()
    ###
    def removeFromChunks(self):
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            for j in range(int(self.topEdge()/self.chunksize), int(self.bottomEdge()/self.chunksize+1)):
                for i in range(int(self.leftEdge()/self.chunksize), int(self.rightEdge()/self.chunksize+1)):
                    self.canvas().removeItemFromChunk(self, i, j)

    ###
    #    The width of the sprite for the current frame's image.
    #
    #    \sa frame()
    ###
    #### mark: Why don't we have width(int) and height(int) to be
    #consistent with leftEdge() and leftEdge(int)?
    def width(self):
        return self.image().width()

    ###
    #    The height of the sprite for the current frame's image.
    #
    #    \sa frame()
    ###
    def height(self):
        return self.image().height()

    ###
    #    Draws the current frame's image at the sprite's current position
    #    on painter \a painter.
    ###
    def draw(self, painter):
        painter.drawPixmap(self.leftEdge(), self.topEdge(), self.image())

    ###
    #    \class QtCanvasView qtcanvas.h
    #    \brief The QtCanvasView class provides an on-screen view of a QtCanvas.
    #
    #    A QtCanvasView is widget which provides a view of a QtCanvas.
    #
    #    If you want users to be able to interact with a canvas view,
    #    subclass QtCanvasView. You might then reimplement
    #    QtScrollView.contentsMousePressEvent(). For example:
    #
    #    \code
    #    def MyCanvasView.contentsMousePressEvent(self, e):
    #        QtCanvasItemList l = canvas().collisions(e.pos())
    #        for (QtCanvasItemList.Iterator it = l.begin(); it!= l.end(); ++it):
    #            if (it.rtti() == QtCanvasRectangle.RTTI):
    #                qDebug("A QtCanvasRectangle lies somewhere at this point")
    #    \endcode
    #
    #    The canvas view shows canvas canvas(); this can be changed using
    #    setCanvas().
    #
    #    A transformation matrix can be used to transform the view of the
    #    canvas in various ways, for example, zooming in or out or rotating.
    #    For example:
    #
    #    \code
    #    QMatrix wm
    #    wm.scale(2, 2);   # Zooms in by 2 times
    #    wm.rotate(90);    # Rotates 90 degrees counter clockwise
    #                        # around the origin.
    #    wm.translate(0, -canvas.height())
    #                        # moves the canvas down so what was visible
    #                        # before is still visible.
    #    myCanvasView.setWorldMatrix(wm)
    #    \endcode
    #
    #    Use setWorldMatrix() to set the canvas view's world matrix: you must
    #    ensure that the world matrix is invertible. The current world matrix
    #    is retrievable with worldMatrix(), and its inversion is retrievable
    #    with inverseWorldMatrix().
    #
    #    Example:
    #
    #    The following code finds the part of the canvas that is visible in
    #    this view, i.e. the bounding rectangle of the view in canvas coordinates.
    #
    #    \code
    #    rc = QRect(myCanvasView.contentsX(), myCanvasView.contentsY(),
    #                        myCanvasView.visibleWidth(), myCanvasView.visibleHeight())
    #    canvasRect = myCanvasView.inverseWorldMatrix().mapRect(rc)
    #    \endcode
    #
    #    \sa QMatrix QPainter.setWorldMatrix()
    #
    ###

class QtCanvasWidget(QWidget):
    def __init__(self, view):
        super(QtCanvasWidget, self).__init__(view)
        self.m_view = view

    def mousePressEvent(self, e):
        self.m_view.contentsMousePressEvent(e)
    def mouseMoveEvent(self, e):
        self.m_view.contentsMouseMoveEvent(e)
    def mouseReleaseEvent(self, e):
        self.m_view.contentsMouseReleaseEvent(e)
    def mouseDoubleClickEvent(self, e):
        self.m_view.contentsMouseDoubleClickEvent(e)
    def dragEnterEvent(self, e):
        self.m_view.contentsDragEnterEvent(e)
    def dragMoveEvent(self, e):
        self.m_view.contentsDragMoveEvent(e)
    def dragLeaveEvent(self, e):
        self.m_view.contentsDragLeaveEvent(e)
    def dropEvent(self, e):
        self.m_view.contentsDropEvent(e)
    def wheelEvent(self, e):
        self.m_view.contentsWheelEvent(e)
    def contextMenuEvent(self, e):
        self.m_view.contentsContextMenuEvent(e)

    def paintEvent(self, e):
        p = QPainter(self)
        if (self.m_view.d.highQuality):
            p.setRenderHint(QPainter.Antialiasing)
            p.setRenderHint(QPainter.SmoothPixmapTransform)
        self.m_view.drawContents(p, e.rect().x(), e.rect().y(), e.rect().width(), e.rect().height())

    ###
    #    Constructs a QtCanvasView with parent \a parent. The canvas view
    #    is not associated with a canvas, so you must to call setCanvas()
    #    to view a canvas.
    ###
class QtCanvasView(QScrollArea):
    def __init__(self, arg1=None, arg2=None):
        if arg2 is None:
            super(QtCanvasView, self).__init__(arg1)
            canvas = 0
        else:
            ###
            #    \overload
            #
            #    Constructs a QtCanvasView which views canvas \a canvas, with parent
            #    \a parent.
            ###
            super(QtCanvasView, self).__init__(arg2)
            canvas = arg1
        self.d = QtCanvasViewData()
        self.d.highQuality = False
        self.setWidget(QtCanvasWidget(self))
        self.viewing = 0
        self.setCanvas(canvas)

    ###
    #    Destroys the canvas view. The associated canvas is \e not deleted.
    ###
    def __del__(self):
        del self.d
        self.d = 0
        self.setCanvas(0)

    ###
    #    \property QtCanvasView.highQualityRendering
    #    \brief whether high quality rendering is turned on
    #
    #    If high quality rendering is turned on, the canvas view will paint itself
    #    using the QPainter.Antialiasing and QPainter.SmoothPixmapTransform
    #    rendering flags.
    #
    #    Enabling these flag will usually improve the visual appearance on the screen
    #    at the cost of rendering speed.
    ###
    def highQualityRendering(self):
        return self.d.highQuality

    def setHighQualityRendering(self, enable):
        self.d.highQuality = enable
        self.widget().update()

    def contentsMousePressEvent(self, e):
        e.ignore()

    def contentsMouseReleaseEvent(self, e):
        e.ignore()

    def contentsMouseDoubleClickEvent(self, e):
        e.ignore()

    def contentsMouseMoveEvent(self, e):
        e.ignore()

    def contentsDragEnterEvent(self):
        pass

    def contentsDragMoveEvent(self):
        pass

    def contentsDragLeaveEvent(self):
        pass

    def contentsDropEvent(self):
        pass

    def contentsWheelEvent(self, e):
        e.ignore()

    def contentsContextMenuEvent(self, e):
        e.ignore()

    ###
    #    \fn QtCanvasView.canvas()
    #
    #    Returns a pointer to the canvas which the QtCanvasView is currently
    #    showing.
    ###
    def canvas(self):
        return self.viewing

    ###
    #    Sets the canvas that the QtCanvasView is showing to the canvas \a
    #    canvas.
    ###
    def setCanvas(self, canvas):
        if (self.viewing == canvas):
            return

        if (self.viewing):
            self.viewing.disconnect()
            self.viewing.removeView(self)
        self.viewing = canvas
        if (self.viewing):
            self.viewing.resized.connect(self.updateContentsSize)
            self.viewing.addView(self)
        if self.d: # called by d'tor
            self.updateContentsSize()
        self.update()

    ###
    #    Returns a reference to the canvas view's current transformation matrix.
    #
    #    \sa setWorldMatrix() inverseWorldMatrix()
    ###
    def worldMatrix(self):
        return self.d.xform

    ###
    #    Returns a reference to the inverse of the canvas view's current
    #    transformation matrix.
    #
    #    \sa setWorldMatrix() worldMatrix()
    ###
    def inverseWorldMatrix(self):
        return self.d.ixform

    ###
    #    Sets the transformation matrix of the QtCanvasView to \a wm. The
    #    matrix must be invertible (i.e. if you create a world matrix that
    #    zooms out by 2 times, then the inverse of this matrix is one that
    #    will zoom in by 2 times).
    #
    #    When you use this, you should note that the performance of the
    #    QtCanvasView will decrease considerably.
    #
    #    Returns False if \a wm is not invertable; otherwise returns True.
    #
    #    \sa worldMatrix() inverseWorldMatrix() QMatrix.isInvertible()
    ###
    def setWorldMatrix(self, wm):
        ok = wm.isInvertible()
        if (ok):
            self.d.xform = wm
            self.d.ixform = wm.inverted()
            self.updateContentsSize()
            self.widget().update()
        return ok

    def updateContentsSize(self):
        if (self.viewing):
            br = self.d.xform.mapRect(QRect(0, 0, self.viewing.width(), self.viewing.height()))

            self.widget().resize(br.size())
        else:
            self.widget().resize(self.size())

    ###
    #    Repaints part of the QtCanvas that the canvas view is showing
    #    starting at \a cx by \a cy, with a width of \a cw and a height of \a
    #    ch using the painter \a p.
    ###
    def drawContents(self, p, cx, cy, cw, ch):
        if (not self.viewing):
            return
        clipPath = QPainterPath()
        clipPath.addRect(QRectF(self.viewing.rect()))
        p.setClipPath(self.d.xform.map(clipPath), Qt.IntersectClip)
        self.viewing.drawViewArea(self, p, QRect(cx, cy, cw, ch), False)

    ###
    #    Suggests a size sufficient to view the entire canvas.
    ###
    def sizeHint(self):
        if (not self.canvas()):
            return QScrollArea.sizeHint()
        # should maybe take transformations into account
        return (self.canvas().size() + 2 * QSize(self.frameWidth(), self.frameWidth())).boundedTo(3 * QApplication.desktop().size() / 4)

    ###
    #    \class QtCanvasPolygonalItem qtcanvas.h
    #    \brief The QtCanvasPolygonalItem class provides a polygonal canvas item
    #    on a QtCanvas.
    #
    #    The mostly rectangular classes, such as QtCanvasSprite and
    #    QtCanvasText, use the object's bounding rectangle for movement, 
    #    repainting and collision calculations. For most other items, the
    #    bounding rectangle can be far too large -- a diagonal line being
    #    the worst case, and there are many other cases which are also bad.
    #    QtCanvasPolygonalItem provides polygon-based bounding rectangle
    #    handling, etc., which is much faster for non-rectangular items.
    #
    #    Derived classes should try to define as small an area as possible
    #    to maximize efficiency, but the polygon must \e definitely be
    #    contained completely within the polygonal area. Calculating the
    #    exact requirements is usually difficult, but if you allow a small
    #    overestimate it can be easy and quick, while still getting almost
    #    all of QtCanvasPolygonalItem's speed.
    #
    #    Note that all subclasses \e must call hide() in their destructor
    #    since hide() needs to be able to access areaPoints().
    #
    #    Normally, QtCanvasPolygonalItem uses the odd-even algorithm for
    #    determining whether an object intersects this object. You can
    #    change this to the winding algorithm using setWinding().
    #
    #    The bounding rectangle is available using boundingRect(). The
    #    points bounding the polygonal item are retrieved with
    #    areaPoints(). Use areaPointsAdvanced() to retrieve the bounding
    #    points the polygonal item \e will have after
    #    QtCanvasItem.advance(1) has been called.
    #
    #    If the shape of the polygonal item is about to change while the
    #    item is visible, call invalidate() before updating with a
    #    different result from \l areaPoints().
    #
    #    By default, QtCanvasPolygonalItem objects have a black pen and no
    #    brush (the default QPen and QBrush constructors). You can change
    #    this with setPen() and setBrush(), but note that some
    #    QtCanvasPolygonalItem subclasses only use the brush, ignoring the
    #    pen setting.
    #
    #    The polygonal item can be drawn on a painter with draw().
    #    Subclasses must reimplement drawShape() to draw themselves.
    #
    #    Like any other canvas item polygonal items can be moved with
    #    QtCanvasItem.move() and QtCanvasItem.moveBy(), or by setting coordinates
    #    with QtCanvasItem.setX(), QtCanvasItem.setY() and QtCanvasItem.setZ().
    #
    ###

    ###
    #  Since most polygonal items don't have a pen, the default is
    #  NoPen and a black brush.
    ###
dp = 0
def defaultPolygonPen():
    global dp
    if (not dp):
        dp = QPen()
    return dp
db = 0
def defaultPolygonBrush():
    global db
    if (not db):
        db = QBrush()
    return db

    ###
    #    Constructs a QtCanvasPolygonalItem on the canvas \a canvas.
    ###
class QtCanvasPolygonalItem(QtCanvasItem):
    def __init__(self, canvas):
        super(QtCanvasPolygonalItem, self).__init__(canvas)

        self.br = defaultPolygonBrush()
        self.pn = defaultPolygonPen()
        self.wind = 0
        self.ani = 0
        self.vis = 0
        self.val = 0
        self.sel = 0
        self.ena = 0
        self.act = 0

    ###
    #    Note that all subclasses \e must call hide() in their destructor
    #    since hide() needs to be able to access areaPoints().
    ###
    def __del__(self):
        pass

    def pen(self):
        return self.pn

    def brush(self):
        return self.br

    def scanPolygon(self, pa, winding, process):
        scanner = QtCanvasPolygonScanner(process)
        scanner.scan(pa, winding)

    def chunks(self):
        pa = self.areaPoints()

        if (not pa.size()):
            #pa.detach() # Explicit sharing is stupid.
            return pa

        processor = QPolygonalProcessor(self.canvas(), pa)

        self.scanPolygon(pa, self.wind, processor)

        return processor.result

    ###
    #    Returns the bounding rectangle of the polygonal item, based on
    #    areaPoints().
    ###
    def boundingRect(self):
        return self.areaPoints().boundingRect()

    ###
    #    Reimplemented from QtCanvasItem, this draws the polygonal item by
    #    setting the pen and brush for the item on the painter \a p and
    #    calling drawShape().
    ###
    def draw(self, p):
        p.setPen(self.pn)
        p.setBrush(self.br)
        self.drawShape(p)

    ###
    #    \fn void QtCanvasPolygonalItem.drawShape(QPainter & p)
    #
    #    Subclasses must reimplement this function to draw their shape. The
    #    pen and brush of \a p are already set to pen() and brush() prior
    #    to calling this function.
    #
    #    \sa draw()
    ###

    ###
    #    \fn QPen QtCanvasPolygonalItem.pen()
    #
    #    Returns the QPen used to draw the outline of the item, if any.
    #
    #    \sa setPen()
    ###

    ###
    #    \fn QBrush QtCanvasPolygonalItem.brush()
    #
    #    Returns the QBrush used to fill the item, if filled.
    #
    #    \sa setBrush()
    ###

    ###
    #    Sets the QPen used when drawing the item to the pen \a p.
    #    Note that many QtCanvasPolygonalItems do not use the pen value.
    #
    #    \sa setBrush(), pen(), drawShape()
    ###
    def setPen(self, p):
        if (self.pn != p):
            if p in [0, None]:
                p = 0
            self.removeFromChunks()
            self.pn = p
            self.addToChunks()

    ###
    #    Sets the QBrush used when drawing the polygonal item to the brush \a b.
    #
    #    \sa setPen(), brush(), drawShape()
    ###
    def setBrush(self, b):
        if (self.br != b):
            self.br = b
            self.changeChunks()

    ###
    #    Returns 2 (RttiValues.Rtti_PolygonalItem).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_PolygonalItem

    ###
    #    \fn bool QtCanvasItem.collidesWith(other)
    #
    #    Returns True if the canvas item will collide with the \a other
    #    item \e after they have moved by their current velocities
    #    otherwise returns False.
    #
    #    \sa collisions()
    ###
    def collidesWith(self, s, *args):
        if len(args) == 0:
            return s.collidesWith(0, self, 0, 0, 0)
        return collision_double_dispatch(s, args[0], args[1], args[2], args[3], 0, self, 0, 0, 0)

    ###
    #    Returns True if the polygonal item uses the winding algorithm to
    #    determine the "inside" of the polygon. Returns False if it uses
    #    the odd-even algorithm.
    #
    #    The default is to use the odd-even algorithm.
    #
    #    \sa setWinding()
    ###
    def winding(self):
        return self.wind

    ###
    #    If \a enable is True, the polygonal item will use the winding
    #    algorithm to determine the "inside" of the polygon; otherwise the
    #    odd-even algorithm will be used.
    #
    #    The default is to use the odd-even algorithm.
    #
    #    \sa winding()
    ###
    def setWinding(self, enable):
        self.wind = enable

    ###
    #    Invalidates all information about the area covered by the canvas
    #    item. The item will be updated automatically on the next call that
    #    changes the item's status, for example, move() or update(). Call
    #    this function if you are going to change the shape of the item (as
    #    returned by areaPoints()) while the item is visible.
    ###
    def invalidate(self):
        self.val = False
        self.removeFromChunks()

    ###
    #    \fn QtCanvasPolygonalItem.isValid()
    #
    #    Returns True if the polygonal item's area information has not been
    #    invalidated; otherwise returns False.
    #
    #    \sa invalidate()
    ###
    def isValid(self):
        return self.val
    ###
    #    Returns the points the polygonal item \e will have after
    #    QtCanvasItem.advance(1) is called, i.e. what the points are when
    #    advanced by the current xVelocity() and yVelocity().
    ###
    def areaPointsAdvanced(self):
        dx = int(self.x()+self.xVelocity())-int(self.x())
        dy = int(self.y()+self.yVelocity())-int(self.y())
        r = self.areaPoints()
        #r.detach(); # Explicit sharing is stupid.
        if (dx or dy):
            r.translate(dx, dy)
        return r

class QPolygonalProcessor():
    def __init__(self, c, pa):
        self.pn = QPen()
        self.br = QBrush()
        self.wind = 1
        self.canvas = c
        self.result = QPolygonEx()
        self.bounds = QRect()
        pixelbounds = pa.boundingRect()
        cs = self.canvas.chunkSize()
        canvasbounds = pixelbounds.intersected(self.canvas.rect())
        self.bounds.setLeft(int(canvasbounds.left()/cs))
        self.bounds.setRight(int(canvasbounds.right()/cs))
        self.bounds.setTop(int(canvasbounds.top()/cs))
        self.bounds.setBottom(int(canvasbounds.bottom()/cs))
        self.bitmap = QImage(self.bounds.width(), self.bounds.height(), QImage.Format_MonoLSB)
        self.pnt = 0
        self.bitmap.fill(0)

    #ifdef QCANVAS_POLYGONS_DEBUG
    #        dbg_start()
    #endif

    def add(self, x, y):
        if (self.pnt >= self.result.size()):
            self.result.resize(self.pnt*2+10)
        self.result[self.pnt] = QPoint(x+self.bounds.x(), y+self.bounds.y())
        self.pnt += 1
    #ifdef QCANVAS_POLYGONS_DEBUG
    #            if (dbg_ptr):
    #                cs = canvas.chunkSize()
    #                r(x*cs+bounds.x()*cs, y*cs+bounds.y()*cs, cs-1, cs-1)
    #                dbg_ptr.setPen(Qt.blue)
    #                dbg_ptr.drawRect(r)
    #endif

    def addBits(self, x1, x2, newbits, xo, yo):
        for i in range(x1, x2+1):
            if (newbits & (1 <<i)):
                self.add(xo+i, yo)

    #ifdef QCANVAS_POLYGONS_DEBUG
    #        def dbg_start(self):
    #            if (not dbg_wid):
    #                dbg_wid = QWidget
    #                dbg_wid.resize(800, 600)
    #                dbg_wid.show()
    #                dbg_ptr = QPainter(dbg_wid)
    #                dbg_ptr.setBrush(Qt.NoBrush)
    #            dbg_ptr.fillRect(dbg_wid.rect(), Qt.white)
    #endif

    def doSpans(self, n, pt, w):
        cs = self.canvas.chunkSize()
        for j in range(n):
            y = int(pt[j].y/cs-self.bounds.y())
            if (y >= self.bitmap.height() or y < 0):
                continue
            l = self.bitmap.scanLine(y).asarray(self.bitmap.bytesPerLine())
            x = int(pt[j].x)
            x1 = int(x/cs-self.bounds.x())
            if (x1 > self.bounds.width()):
                continue
            x1 = max(0,x1)
            x2 = int((x+w[j])/cs-self.bounds.x())
            if (x2 < 0):
                continue
            x2 = min(self.bounds.width(), x2)
            x1q = int(x1/8)
            x1r = int(x1%8)
            x2q = int(x2/8)
            x2r = int(x2%8)
    #ifdef QCANVAS_POLYGONS_DEBUG
    #                if (dbg_ptr) dbg_ptr.setPen(Qt.yellow):
    #endif
            if (x1q == x2q):
                newbits = (~l[x1q]) & (((2 <<(x2r-x1r))-1) <<x1r)
                if (newbits):
    #ifdef QCANVAS_POLYGONS_DEBUG
    #                        if (dbg_ptr) dbg_ptr.setPen(Qt.darkGreen):
    #endif
                    self.addBits(x1r, x2r, newbits, x1q*8, y)
                    l[x1q] |= newbits
            else:
    #ifdef QCANVAS_POLYGONS_DEBUG
    #                    if (dbg_ptr) dbg_ptr.setPen(Qt.blue):
    #endif
                newbits1 = (~l[x1q]) & (0xff <<x1r)
                if (newbits1):
    #ifdef QCANVAS_POLYGONS_DEBUG
    #                        if (dbg_ptr) dbg_ptr.setPen(Qt.green):
    #endif
                    self.addBits(x1r, 7, newbits1, x1q*8, y)
                    l[x1q] |= newbits1
                for i in range(x1q+1, x2q):
                    if (l[i] != 0xff):
                        self.addBits(0, 7, ~l[i], i*8, y)
                        l[i] = 0xff
                newbits2 = (~l[x2q]) & (0xff>>(7-x2r))
                if (newbits2):
    #ifdef QCANVAS_POLYGONS_DEBUG
    #                        if (dbg_ptr) dbg_ptr.setPen(Qt.red):
    #endif
                    self.addBits(0, x2r, newbits2, x2q*8, y)
                    l[x2q] |= newbits2
    #ifdef QCANVAS_POLYGONS_DEBUG
    #                if (dbg_ptr):
    #                    dbg_ptr.drawLine(pt[j], pt[j]+QPoint(w[j], 0))
    #endif
        self.result.resize(self.pnt)

###
#    \class QtCanvasPolygon qtcanvas.h
#    \brief The QtCanvasPolygon class provides a polygon on a QtCanvas.
#
#    Paints a polygon with a QBrush. The polygon's points can be set in
#    the constructor or set or changed later using setPoints(). Use
#    points() to retrieve the points, or areaPoints() to retrieve the
#    points relative to the canvas's origin.
#
#    The polygon can be drawn on a painter with drawShape().
#
#    Like any other canvas item polygons can be moved with
#    QtCanvasItem.move() and QtCanvasItem.moveBy(), or by setting
#    coordinates with QtCanvasItem.setX(), QtCanvasItem.setY() and
#    QtCanvasItem.setZ().
#
#    Note: QtCanvasPolygon does not use the pen.
###
class QtCanvasPolygon(QtCanvasPolygonalItem):
    ###
    #    Constructs a point-less polygon on the canvas \a canvas. You
    #    should call setPoints() before using it further.
    ###
    def __init__(self, canvas):
        super(QtCanvasPolygon, self).__init__(canvas)

        self.poly = QPolygonEx()
        self.current_canvas = None
        self.ext = None
        self.cnv = canvas
        self.myx = 0
        self.myy = 0
        self.myz = 0

        self.ani = 0
        self.vis = 0
        self.val = 0
        self.sel = 0
        self.ena = 0
        self.act = 0

        self.ext = 0
        if self.cnv:
            self.cnv.addItem(self)
    ###
    #    Destroys the polygon.
    ###
    def __del__(self):
        self.hide()

    ###
    #    Returns 4 (RttiValues.Rtti_Polygon).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Polygon

    ###
    #    Draws the polygon using the painter \a p.
    #
    #    Note that QtCanvasPolygon does not support an outline (the pen is
    #    always NoPen).
    ###
    def drawShape(self, p):
        # ### why can't we draw outlines? We could use drawPolyline for it. Lars
        # ### see other message. Warwick

        p.setPen(QPen(Qt.NoPen)); # since QRegion(QPolygon) excludes outline :-()-:
        p.drawPolygon(self.poly)

    ###
    #    Sets the points of the polygon to be \a pa. These points will have
    #    their x and y coordinates automatically translated by x(), y() as
    #    the polygon is moved.
    ###
    def setPoints(self, pa):
        self.removeFromChunks()
        poly = pa
        #poly.detach() # Explicit sharing is stupid.
        poly.translate(self.x(), self.y())
        self.addToChunks()

    ###
    #  \reimp
    ###
    def moveBy(self, dx, dy):
        # Note: does NOT call QtCanvasPolygonalItem.moveBy(), since that
        # only does half this work.
        #
        idx = int(self.x()+dx)-int(self.x())
        idy = int(self.y()+dy)-int(self.y())
        if (idx or idy):
            self.removeFromChunks()
            self.poly.translate(idx, idy)
        self.myx += dx
        self.myy += dy
        if (idx or idy):
            self.addToChunks()

###
#    \class QtCanvasSpline qtcanvas.h
#    \brief The QtCanvasSpline class provides multi-bezier splines on a QtCanvas.
#
#    A QtCanvasSpline is a sequence of 4-point bezier curves joined
#    together to make a curved shape.
#
#    You set the control points of the spline with setControlPoints().
#
#    If the bezier is closed(), then the first control point will be
#    re-used as the last control point. Therefore, a closed bezier must
#    have a multiple of 3 control points and an open bezier must have
#    one extra point.
#
#    The beziers are not necessarily joined "smoothly". To ensure this,
#    set control points appropriately (general reference texts about
#    beziers will explain this in detail).
#
#    Like any other canvas item splines can be moved with
#    QtCanvasItem.move() and QtCanvasItem.moveBy(), or by setting
#    coordinates with QtCanvasItem.setX(), QtCanvasItem.setY() and
#    QtCanvasItem.setZ().
#
###
class QtCanvasSpline(QtCanvasPolygon):
    ###
    #    Create a spline with no control points on the canvas \a canvas.
    #
    #    \sa setControlPoints()
    ###
    def __init__(self, canvas):
        super(QtCanvasSpline, self).__init__(canvas)

        self.cl = True

    ###
    #    Destroy the spline.
    ###
    def __del__(self):
        pass

    ###
    #    Returns 8 (RttiValues.Rtti_Spline).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Spline

    ###
    #    Set the spline control points to \a ctrl.
    #
    #    If \a close is True, then the first point in \a ctrl will be
    #    re-used as the last point, and the number of control points must
    #    be a multiple of 3. If \a close is False, one additional control
    #    point is required, and the number of control points must be one of
    #    (4, 7, 10, 13, ...).
    #
    #    If the number of control points doesn't meet the above conditions, 
    #    the number of points will be truncated to the largest number of
    #    points that do meet the requirement.
    ###
    def setControlPoints(self, ctrl, close):
        x = 1
        if close:
            x = 0
        if (ctrl.count() % 3 != x):
            qWarning("QtCanvasSpline.setControlPoints(): Number of points doesn't fit.")
            numCurves = (ctrl.count() - x)/ 3
            ctrl.resize(numCurves*3 + x)

        self.cl = close
        self.bez = ctrl
        self.recalcPoly()

    ###
    #    Returns the current set of control points.
    #
    #    \sa setControlPoints(), closed()
    ###
    def controlPoints(self):
        return self.bez

    ###
    #    Returns True if the control points are a closed set; otherwise
    #    returns False.
    ###
    def closed(self):
        return self.cl

    def recalcPoly(self):
        if (self.bez.count() == 0):
            return

        path = QPainterPath()
        path.moveTo(self.bez[0])

        for i in range(1, self.bez.count()-1, 3):
            if self.cl:
                path.cubicTo(self.bez[i], self.bez[i+1], self.bez[(i+2)%self.bez.size()])
            else:
                path.cubicTo(self.bez[i], self.bez[i+1], self.bez[i+2])

        p = path.toFillPolygon().toPolygon()
        super(QtCanvasSpline, self).setPoints(p)

    ###
    #    \fn QPolygon QtCanvasPolygonalItem.areaPoints()
    #
    #    This function must be reimplemented by subclasses. It \e must
    #    return the points bounding (i.e. outside and not touching) the
    #    shape or drawing errors will occur.
    ###

    ###
    #    \fn QPolygon QtCanvasPolygon.points()
    #
    #    Returns the vertices of the polygon, not translated by the position.
    #
    #    \sa setPoints(), areaPoints()
    ###
    def points(self):
        pa = self.areaPoints()
        pa.translate(int(-self.x()), int(-self.y()))
        return pa

    ###
    #    Returns the vertices of the polygon translated by the polygon's
    #    current x(), y() position, i.e. relative to the canvas's origin.
    #
    #    \sa setPoints(), points()
    ###
    def areaPoints(self):
        return self.poly

###
#    \class QtCanvasLine qtcanvas.h
#    \brief The QtCanvasLine class provides a line on a QtCanvas.
#
#    The line inherits functionality from QtCanvasPolygonalItem, for
#    example the setPen() function. The start and end points of the
#    line are set with setPoints().
#
#    Like any other canvas item lines can be moved with
#    QtCanvasItem.move() and QtCanvasItem.moveBy(), or by setting
#    coordinates with QtCanvasItem.setX(), QtCanvasItem.setY() and
#    QtCanvasItem.setZ().
###
class QtCanvasLine(QtCanvasPolygonalItem):
    ###
    #    Constructs a line from (0, 0) to (0, 0) on \a canvas.
    #
    #    \sa setPoints()
    ###
    def __init__(self, canvas):
        super(QtCanvasLine, self).__init__(canvas)

        self.x1 = self.y1 = self.x2 = self.y2 = 0

    def startPoint(self):
        return QPoint(self.x1, self.y1)

    def endPoint(self):
        return QPoint(self.x2, self.y2)

    ###
    #    Destroys the line.
    ###
    def __del__(self):
        self.hide()

    ###
    #    Returns 7 (RttiValues.Rtti_Line).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Line

    ###
    #  \reimp
    ###
    def setPen(self, p):
        super(QtCanvasLine, self).setPen(p)

    ###
    #    \fn QPoint QtCanvasLine.startPoint ()
    #
    #    Returns the start point of the line.
    #
    #    \sa setPoints(), endPoint()
    ###

    ###
    #    \fn QPoint QtCanvasLine.endPoint ()
    #
    #    Returns the end point of the line.
    #
    #    \sa setPoints(), startPoint()
    ###

    ###
    #    Sets the line's start point to (\a xa, \a ya) and its end point to
    #    (\a xb, \a yb).
    ###
    def setPoints(self, xa, ya, xb, yb):
        if (self.x1 != xa or self.x2 != xb or self.y1 != ya or self.y2 != yb):
            self.removeFromChunks()
            self.x1 = xa
            self.y1 = ya
            self.x2 = xb
            self.y2 = yb
            self.addToChunks()

    ###
    #  \reimp
    ###
    def drawShape(self, p):
        p.drawLine((self.x()+self.x1), (self.y()+self.y1), (self.x()+self.x2), (self.y()+self.y2))

    ###
    #    \reimp
    #
    #    Note that the area defined by the line is somewhat thicker than
    #    the line that is actually drawn.
    ###
    def areaPoints(self):
        p = QPolygonEx(4)
        xi = int(self.x())
        yi = int(self.y())
        pw = self.pen().width()
        dx = abs(self.x1-self.x2)
        dy = abs(self.y1-self.y2)
        pw = pw*4/3+2; # approx pw*sqrt(2)
        if self.x1 < self.x2:
            px = -pw
        else:
            px = pw
        if self.y1 < self.y2:
            py = -pw
        else:
            py = pw
        if dx>0 and dy>0:
            if dx > dy:
                _dxy = dx*2/dy <= 2
            else:
                _dxy = dy*2/dx <= 2

            if _dxy:
                # steep
                if (px == py):
                    p[0] = QPoint(self.x1+xi, self.y1+yi+py)
                    p[1] = QPoint(self.x2+xi-px, self.y2+yi)
                    p[2] = QPoint(self.x2+xi, self.y2+yi-py)
                    p[3] = QPoint(self.x1+xi+px, self.y1+yi)
                else:
                    p[0] = QPoint(self.x1+xi+px, self.y1+yi)
                    p[1] = QPoint(self.x2+xi, self.y2+yi-py)
                    p[2] = QPoint(self.x2+xi-px, self.y2+yi)
                    p[3] = QPoint(self.x1+xi, self.y1+yi+py)
            elif (dx > dy):
                # horizontal
                p[0] = QPoint(self.x1+xi+px, self.y1+yi+py)
                p[1] = QPoint(self.x2+xi-px, self.y2+yi+py)
                p[2] = QPoint(self.x2+xi-px, self.y2+yi-py)
                p[3] = QPoint(self.x1+xi+px, self.y1+yi-py)
            else:
                # vertical
                p[0] = QPoint(self.x1+xi+px, self.y1+yi+py)
                p[1] = QPoint(self.x2+xi+px, self.y2+yi-py)
                p[2] = QPoint(self.x2+xi-px, self.y2+yi-py)
                p[3] = QPoint(self.x1+xi-px, self.y1+yi+py)
        return p

    ###
    #    \reimp
    #
    ###

    def moveBy(self, dx, dy):
        super(QtCanvasLine, self).moveBy(dx, dy)

###
#    \class QtCanvasRectangle qtcanvas.h
#    \brief The QtCanvasRectangle class provides a rectangle on a QtCanvas.
#
#    This item paints a single rectangle which may have any pen() and
#    brush(), but may not be tilted/rotated. For rotated rectangles,
#    use QtCanvasPolygon.
#
#    The rectangle's size and initial position can be set in the
#    constructor. The size can be set or changed later using setSize().
#    Use height() and width() to retrieve the rectangle's dimensions.
#
#    The rectangle can be drawn on a painter with drawShape().
#
#    Like any other canvas item rectangles can be moved with
#    QtCanvasItem.move() and QtCanvasItem.moveBy(), or by setting
#    coordinates with QtCanvasItem.setX(), QtCanvasItem.setY() and
#    QtCanvasItem.setZ().
#
###
class QtCanvasRectangle(QtCanvasPolygonalItem):
    def __init__(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        if type(arg1)==QtCanvas:
            ###
            #    Constructs a rectangle at position (0,0) with both width and
            #    height set to 32 pixels on \a canvas.
            ###
            super(QtCanvasRectangle, self).__init__(arg1)
            self.w = 32
            self.h = 32
        elif type(arg2)==QtCanvas:
            ###
            #    Constructs a rectangle positioned and sized by \a r on \a canvas.
            ###
            super(QtCanvasRectangle, self).__init__(arg2)
            self.w = arg1.width()
            self.h = arg1.height()
            self.move(arg1.x(), arg1.y())
        elif type(arg5)==QtCanvas:
            ###
            #    Constructs a rectangle at position (\a x, \a y) and size \a width
            #    by \a height, on \a canvas.
            ###
            super(QtCanvasRectangle, self).__init__(arg5)
            self.w = arg3
            self.h = arg4
            self.move(arg1, arg2)

    def size(self):
        return QSize(self.w, self.h)

    def rect(self):
        return QRect(int(self.x()), int(self.y()), self.w, self.h)
    ###
    #    Destroys the rectangle.
    ###
    def __del__(self):
        self.hide()

    ###
    #    Simply calls QtCanvasItem.chunks().
    ###
    def chunks(self):
        # No need to do a polygon scan!
        return super(QtCanvasPolygonalItem, self).chunks()

    ###
    #    Returns 5 (RttiValues.Rtti_Rectangle).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Rectangle

    ###
    #  \reimp
    ###
    def collidesWith(self, s, *args):
        if len(args) == 0:
            return s.collidesWith(0, self, self, 0, 0)
        return collision_double_dispatch(s, args[0], args[1], args[2], args[3], 0, self, self, 0, 0)

    ###
    #    Returns the width of the rectangle.
    ###
    def width(self):
        return self.w

    ###
    #    Returns the height of the rectangle.
    ###
    def height(self):
        return self.h

    ###
    #    Sets the \a width and \a height of the rectangle.
    ###
    def setSize(self, width, height):
        if (self.w != width or self.h != height):
            self.removeFromChunks()
            self.w = width
            self.h = height
            self.addToChunks()

    ###
    #    \fn QSize QtCanvasRectangle.size()
    #
    #    Returns the width() and height() of the rectangle.
    #
    #    \sa rect(), setSize()
    ###

    ###
    #    \fn QRect QtCanvasRectangle.rect()
    #
    #    Returns the integer-converted x(), y() position and size() of the
    #    rectangle as a QRect.
    ###

    ###
    #  \reimp
    ###
    def areaPoints(self):
        pa = QPolygonEx(4)
        pw = (self.pen().width()+1)/2
        if (pw < 1):
            pw = 1
        if (self.pen() == Qt.NoPen):
            pw = 0
        pa[0] = QPoint(self.x()-pw, self.y()-pw)
        pa[1] = pa[0] + QPoint(self.w+pw*2, 0)
        pa[2] = pa[1] + QPoint(0, self.h+pw*2)
        pa[3] = pa[0] + QPoint(0, self.h+pw*2)
        return pa

    ###
    #    Draws the rectangle on painter \a p.
    ###
    def drawShape(self, p):
        p.drawRect(self.x(), self.y(), self.w, self.h)

###
#    \class QtCanvasEllipse qtcanvas.h
#    \brief The QtCanvasEllipse class provides an ellipse or ellipse segment on a QtCanvas.
#
#    A canvas item that paints an ellipse or ellipse segment with a QBrush.
#    The ellipse's height, width, start angle and angle length can be set
#    at construction time. The size can be changed at runtime with
#    setSize(), and the angles can be changed (if you're displaying an
#    ellipse segment rather than a whole ellipse) with setAngles().
#
#    Note that angles are specified in 16ths of a degree.
#
#    \target anglediagram
#    \img qcanvasellipse.png Ellipse
#
#    If a start angle and length angle are set then an ellipse segment
#    will be drawn. The start angle is the angle that goes from zero in a
#    counter-clockwise direction (shown in green in the diagram). The
#    length angle is the angle from the start angle in a
#    counter-clockwise direction (shown in blue in the diagram). The blue
#    segment is the segment of the ellipse that would be drawn. If no
#    start angle and length angle are specified the entire ellipse is
#    drawn.
#
#    The ellipse can be drawn on a painter with drawShape().
#
#    Like any other canvas item ellipses can be moved with move() and
#    moveBy(), or by setting coordinates with setX(), setY() and setZ().
#
#    Note: QtCanvasEllipse does not use the pen.
###
class QtCanvasEllipse(QtCanvasPolygonalItem):
    def __init__(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        t = type(arg1)
        if t==QtCanvas:
            ###
            #    Constructs a 32x32 ellipse, centered at (0, 0) on \a canvas.
            ###
            self.w = 32
            self.h = 32
            self.a1 = 0
            self.a2 = 360*16
            canvas = arg1
        elif t==int:
            t = type(arg3)
            if t==QtCanvas:
                ###
                #    Constructs a \a width by \a height pixel ellipse, centered at
                #    (0, 0) on \a canvas.
                ###
                self.w = arg1
                self.h = arg2
                self.a1 = 0
                self.a2 = 360*16
                canvas = arg3
            elif t==int:
                # ### add a constructor taking degrees in float. 1/16 degrees is stupid. Lars
                # ### it's how QPainter does it, so QtCanvas does too for consistency. If it's
                # ###  a good idea, it should be added to QPainter, not just to QtCanvas. Warwick
                ###
                #    Constructs a \a width by \a height pixel ellipse, centered at
                #    (0, 0) on \a canvas. Only a segment of the ellipse is drawn,
                #    starting at angle \a startangle, and extending for angle \a angle
                #    (the angle length).
                #
                #    Note that angles are specified in sixteenths of a degree.
                ###
                self.w = arg1
                self.h = arg2
                self.a1 = arg3
                self.a2 = arg4
                canvas = arg5
        super(QtCanvasEllipse, self).__init__(canvas)

    ###
    #    Destroys the ellipse.
    ###
    def __del__(self):
        self.hide()

    ###
    #    Returns 6 (RttiValues.Rtti_Ellipse).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Ellipse

    ###
    #  \reimp
    ###
    def collidesWith(self, s, *args):
        if len(args) == 0:
            return s.collidesWith(0,self, 0, self, 0)
        return collision_double_dispatch(s, args[0], args[1], args[2], args[3], 0, self, 0, self, 0)
    ###
    #    Returns the width of the ellipse.
    ###
    def width(self):
        return self.w

    ###
    #    Returns the height of the ellipse.
    ###
    def height(self):
        return self.h

    ###
    #    Sets the \a width and \a height of the ellipse.
    ###
    def setSize(self, width, height):
        if (self.w != width or self.h != height):
            self.removeFromChunks()
            self.w = width
            self.h = height
            self.addToChunks()

    ###
    #    \fn int QtCanvasEllipse.angleStart()
    #
    #    Returns the start angle in 16ths of a degree. Initially
    #    this will be 0.
    #
    #    \sa setAngles(), angleLength()
    ###

    ###
    #    \fn int QtCanvasEllipse.angleLength()
    #
    #    Returns the length angle (the extent of the ellipse segment) in
    #    16ths of a degree. Initially this will be 360 * 16 (a complete
    #    ellipse).
    #
    #    \sa setAngles(), angleStart()
    ###

    ###
    #    Sets the angles for the ellipse. The start angle is \a start and
    #    the extent of the segment is \a length (the angle length) from the
    #    \a start. The angles are specified in 16ths of a degree. By
    #    default the ellipse will start at 0 and have an angle length of
    #    360 * 16 (a complete ellipse).
    #
    #    \sa angleStart(), angleLength()
    ###
    def setAngles(self, start, length):
        if (self.a1 != start or self.a2 != length):
            self.removeFromChunks()
            self.a1 = start
            self.a2 = length
            self.addToChunks()

    ###
    #  \reimp
    ###
    def areaPoints(self):
        path = QPainterPath()
        path.arcTo(QRectF(self.x()-self.w/2.0+0.5-1, self.y()-self.h/2.0+0.5-1, self.w+3, self.h+3), self.a1/16., self.a2/16.)
        return path.toFillPolygon(QMatrix()).toPolygon()

    ###
    #    Draws the ellipse, centered at x(), y() using the painter \a p.
    #
    #    Note that QtCanvasEllipse does not support an outline (the pen is
    #    always NoPen).
    ###
    def drawShape(self, p):
        p.setPen(QPen(Qt.NoPen)); # since QRegion(QPolygon) excludes outline :-()-:
        if (not self.a1 and self.a2 == 360*16):
            p.drawEllipse(int(self.x()-self.w/2.0+0.5), int(self.y()-self.h/2.0+0.5), self.w, self.h)
        else:
            p.drawPie(int(self.x()-self.w/2.0+0.5), int(self.y()-self.h/2.0+0.5), self.w, self.h, self.a1, self.a2)

###
#    \class QtCanvasText
#    \brief The QtCanvasText class provides a text object on a QtCanvas.
#
#    A canvas text item has text with font, color and alignment
#    attributes. The text and font can be set in the constructor or set
#    or changed later with setText() and setFont(). The color is set
#    with setColor() and the alignment with setTextFlags(). The text
#    item's bounding rectangle is retrieved with boundingRect().
#
#    The text can be drawn on a painter with draw().
#
#    Like any other canvas item text items can be moved with
#    QtCanvasItem.move() and QtCanvasItem.moveBy(), or by setting
#    coordinates with QtCanvasItem.setX(), QtCanvasItem.setY() and
#    QtCanvasItem.setZ().
###
class QtCanvasText(QtCanvasItem):
    def __init__(self, arg1, arg2=None, arg3=None):
        self.brect = QRect()
        self.txt = ''
        self.flags = 0
        self.fnt = QFont()
        self.col = QColor()
        t1 = type(arg1)
        t2 = type(arg2)
        t3 = type(arg3)
        if t1==QtCanvas:
            ###
            #    Constructs a QtCanvasText with the text "\<text\>", on \a canvas.
            ###
            self.txt = "<text>"
            canvas = arg1
        elif t2==QtCanvas:
            # ### add textflags to the constructor? Lars
            ###
            #    Constructs a QtCanvasText with the text \a t, on canvas \a canvas.
            ###
            self.txt = arg1
            canvas = arg2
        elif t3==QtCanvas:
            # ### see above
            ###
            #    Constructs a QtCanvasText with the text \a t and font \a f, on the
            #    canvas \a canvas.
            ###
            self.txt = arg1
            self.fnt = arg2
            canvas = arg3
        super(QtCanvasText, self).__init__(canvas)
        self.flags = 0
        self.setRect()

    ###
    #    Destroys the canvas text item.
    ###
    def __del__(self):
        self.removeFromChunks()

    ###
    #    Returns 3 (RttiValues.Rtti_Text).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Text

    ###
    #  \reimp
    ###
    def collidesWith(self, s, *args):
        if len(args) == 0:
            return s.collidesWith(0, 0, 0, 0, self)
        return collision_double_dispatch(s, args[0], args[1], args[2], args[3], 0, 0, 0, 0, self)
    ###
    #    Returns the bounding rectangle of the text.
    ###
    def boundingRect(self):
        return self.brect

    def setRect(self):
        self.brect = QFontMetrics(self.fnt).boundingRect(int(self.x()), int(self.y()), 0, 0, self.flags, self.txt)

    ###
    #    \fn int QtCanvasText.textFlags()
    #
    #    Returns the currently set alignment flags.
    #
    #    \sa setTextFlags() Qt.AlignmentFlag Qt.TextFlag
    ###

    ###
    #    Sets the alignment flags to \a f. These are a bitwise OR of the
    #    flags available to QPainter.drawText() -- see the
    #    \l{Qt.AlignmentFlag}s and \l{Qt.TextFlag}s.
    #
    #    \sa setFont() setColor()
    ###
    def setTextFlags(self, f):
        if (self.flags != f):
            self.removeFromChunks()
            self.flags = f
            self.setRect()
            self.addToChunks()

    ###
    #    Returns the text item's text.
    #
    #    \sa setText()
    ###
    def text(self):
        return self.txt

    ###
    #    Sets the text item's text to \a t. The text may contain newlines.
    #
    #    \sa text(), setFont(), setColor() setTextFlags()
    ###
    def setText(self, t):
        if (self.txt != t):
            self.removeFromChunks()
            self.txt = t
            self.setRect()
            self.addToChunks()

    ###
    #    Returns the font in which the text is drawn.
    #
    #    \sa setFont()
    ###
    def font(self):
        return self.fnt

    ###
    #    Sets the font in which the text is drawn to font \a f.
    #
    #    \sa font()
    ###
    def setFont(self, f):
        if (f != self.fnt):
            self.removeFromChunks()
            self.fnt = f
            self.setRect()
            self.addToChunks()

    ###
    #    Returns the color of the text.
    #
    #    \sa setColor()
    ###
    def color(self):
        return self.col

    ###
    #    Sets the color of the text to the color \a c.
    #
    #    \sa color(), setFont()
    ###
    def setColor(self, c):
        self.col = c
        self.changeChunks()

    ###
    #  \reimp
    ###
    def moveBy(self, dx, dy):
        idx = int(self.x()+dx)-int(self.x())
        idy = int(self.y()+dy)-int(self.y())
        if (idx or idy):
            self.removeFromChunks()
        self.myx += dx
        self.myy += dy
        if (idx or idy):
            self.brect.translate(idx, idy)
            self.addToChunks()

    ###
    #    Draws the text using the painter \a painter.
    ###
    def draw(self, painter):
        painter.setFont(self.fnt)
        painter.setPen(self.col)
        painter.drawText(painter.fontMetrics().boundingRect(int(self.x()), int(self.y()), 0, 0, self.flags, self.txt), self.flags, self.txt)

    ###
    #  \reimp
    ###
    def changeChunks(self):
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            for j in range(int(self.brect.top()/self.chunksize), int(self.brect.bottom()/self.chunksize+1)):
                for i in range(int(self.brect.left()/self.chunksize), int(self.brect.right()/self.chunksize+1)):
                    self.canvas().setChangedChunk(i, j)

    ###
    #    Adds the text item to the appropriate chunks.
    ###
    def addToChunks(self):
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            for j in range(int(self.brect.top()/self.chunksize), int(self.brect.bottom()/self.chunksize+1)):
                for i in range(int(self.brect.left()/self.chunksize), int(self.brect.right()/self.chunksize+1)):
                    self.canvas().addItemToChunk(self, i, j)

    ###
    #    Removes the text item from the appropriate chunks.
    ###
    def removeFromChunks(self):
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            for j in range(int(self.brect.top()/self.chunksize), int(self.brect.bottom()/self.chunksize+1)):
                for i in range(int(self.brect.left()/self.chunksize), int(self.brect.right()/self.chunksize+1)):
                    self.canvas().removeItemFromChunk(self, i, j)

class QtCanvasSprite(QtCanvasItem):
    ###
    #    Constructs a QtCanvasSprite which uses images from the
    #    QtCanvasPixmapArray \a a.
    #
    #    The sprite in initially positioned at (0, 0) on \a canvas, using
    #    frame 0.
    ###
    def __init__(self, a, canvas):
        super(QtCanvasSprite, self).__init__(canvas)

        self.frm = 0
        self.anim_val = 0
        self.anim_state = 0
        self.anim_type = 0
        self.images = a

    ###
    #    Returns 1 (RttiValues.Rtti_Sprite).
    #
    #    \sa QtCanvasItem.rtti()
    ###
    def rtti(self):
        return self.RTTI
    RTTI = RttiValues.Rtti_Sprite

    def image(self):
        return self.images.image(self.frm)
    ###
    #    Returns True if the canvas item collides with any of the given
    #    items; otherwise returns False. The parameters, \a s, \a p, \a r,
    #    \a e and \a t, are all the same object, this is just a type
    #    resolution trick.
    ###
    def collidesWith(self, s, *args):
        if len(args) == 0:
            return s.collidesWith(self, 0, 0, 0, 0)
        return collision_double_dispatch(s, args[0], args[1], args[2], args[3], self, 0, 0, 0, 0) 
    ###
    #    Set the array of images used for displaying the sprite to the
    #    QtCanvasPixmapArray \a a.
    #
    #    If the current frame() is larger than the number of images in \a
    #    a, the current frame will be reset to 0.
    ###
    def setSequence(self, a):
        isvisible = self.isVisible()
        if (isvisible and self.images):
            self.hide()
        images = a
        if (self.frm >= images.count()):
            self.frm = 0
        if (isvisible):
            self.show()

    ###
    #\internal
    #
    #Marks any chunks the sprite touches as changed.
    ###
    def changeChunks(self):
        if (self.isVisible() and self.canvas()):
            self.chunksize = self.canvas().chunkSize()
            for j in range(int(self.topEdge()/self.chunksize, self.bottomEdge()/self.chunksize+1)):
                for i in range(int(self.leftEdge()/self.chunksize, self.rightEdge()/self.chunksize+1)):
                    self.canvas().setChangedChunk(i, j)

    ###
    #    Destroys the sprite and removes it from the canvas. Does \e not
    #    del the images.
    ###
    def __del__(self):
        self.removeFromChunks()
        
    def frame(self):
        return self.frm

    def frameCount(self):
        return self.images.count()
    ###
    #    Sets the animation frame used for displaying the sprite to \a f, 
    #    an index into the QtCanvasSprite's QtCanvasPixmapArray. The call
    #    will be ignored if \a f is larger than frameCount() or smaller
    #    than 0.
    #
    #    \sa frame() move()
    ###
    def setFrame(self, f):
        self.move(self.x(), self.y(), f)

    ###
    #    \enum QtCanvasSprite.FrameAnimationType
    #
    #    This enum is used to identify the different types of frame
    #    animation offered by QtCanvasSprite.
    #
    #    \value Cycle at each advance the frame number will be incremented by
    #    1 (modulo the frame count).
    #    \value Oscillate at each advance the frame number will be
    #    incremented by 1 up to the frame count then decremented to by 1 to
    #    0, repeating this sequence forever.
    ###

    ###
    #    Sets the animation characteristics for the sprite.
    #
    #    For \a type == \c Cycle, the frames will increase by \a step
    #    at each advance, modulo the frameCount().
    #
    #    For \a type == \c Oscillate, the frames will increase by \a step
    #    at each advance, up to the frameCount(), then decrease by \a step
    #    back to 0, repeating forever.
    #
    #    The \a state parameter is for internal use.
    ###
    def setFrameAnimation(self, type, step=1, state=0):
        self.anim_val = step
        self.anim_type = type
        self.anim_state = state
        self.setAnimated(True)

    ###
    #    Extends the default QtCanvasItem implementation to provide the
    #    functionality of setFrameAnimation().
    #
    #    The \a phase is 0 or 1: see QtCanvasItem.advance() for details.
    #
    #    \sa QtCanvasItem.advance() setVelocity()
    ###
    def advance(self, phase):
        if (phase == 1):
            nf = self.frame()
            if (self.anim_type == self.Oscillate):
                if (self.anim_state):
                    nf += self.anim_val
                else:
                    nf -= self.anim_val
                if (nf < 0):
                    nf = abs(self.anim_val)
                    self.anim_state = not self.anim_state
                elif (nf >= self.frameCount()):
                    nf = self.frameCount()-1-abs(self.anim_val)
                    self.anim_state = not self.anim_state
            else:
                nf = (nf + self.anim_val + self.frameCount()) % self.frameCount()
            self.move(self.x()+self.xVelocity(), self.y()+self.yVelocity(), nf)

    ###
    #    \fn int QtCanvasSprite.frame()
    #
    #    Returns the index of the current animation frame in the
    #    QtCanvasSprite's QtCanvasPixmapArray.
    #
    #    \sa setFrame(), move()
    ###

    ###
    #    \fn int QtCanvasSprite.frameCount()
    #
    #    Returns the number of frames in the QtCanvasSprite's
    #    QtCanvasPixmapArray.
    ###

    ###
    #    \fn void QtCanvasSprite.move(double nx, ny, nf)
    #
    #    Moves the sprite to (\a nx, \a ny) and sets the current
    #    frame to \a nf. \a nf will be ignored if it is larger than
    #    frameCount() or smaller than 0.
    ###
    def move(self, nx, ny, nf=None):
        if nf is None:
            ###
            #    Moves the sprite to (\a x, \a y).
            ###
            super(QtCanvasSprite, self).move(self, nx, ny)
        else:
            if (self.isVisible() and self.canvas()):
                self.hide()
                super(QtCanvasSprite, self).move(nx, ny)
                if (nf >= 0 and nf < self.frameCount()):
                    self.frm = nf
                self.show()
            else:
                super(QtCanvasSprite, self).move(nx, ny)
                if (nf >= 0 and nf < self.frameCount()):
                    self.frm = nf

class QtPolygonScanner():
    def __del__(self):
        pass

    class Edge(Enum):
        Left = 1
        Right = 2
        Top = 4
        Bottom = 8

    ###
    #    \overload
    #
    #    If \a stitchable is False, the right and bottom edges of the
    #    polygon are included. This causes adjacent polygons to overlap.
    ###
    def scan(self, pa, winding, index=0, npoints=-1, stitchable=True):
        if stitchable:
            edge = Edge.Left.value+Edge.Top.value
        else:
            edge = Edge.Left.value+Edge.Right.value+Edge.Top.value+Edge.Bottom.value

        self.__scan(pa, winding, index, npoints, edge)

    ###
    #    Calls processSpans() for all scanlines of the polygon defined by
    #    \a npoints starting at \a index in \a pa.
    #
    #    If \a winding is True, the Winding algorithm rather than the
    #    Odd-Even rule is used.
    #
    #    The \a edges is any bitwise combination of:
    #    \list
    #    \i QtPolygonScanner.Left
    #    \i QtPolygonScanner.Right
    #    \i QtPolygonScanner.Top
    #    \i QtPolygonScanner.Bottom
    #    \endlist
    #    \a edges determines which edges are included.
    #
    #    \warning The edges feature does not work properly.
    #
    ###
    def __scan(self, pa, winding, index, npoints, edges):
        ptsIn = pa
        pAET = None                     ### the Active Edge Table   ###
        y = 0                           ### the current scanline    ###
        nPts = 0                        ### number of pts in buffer ###
        pWETE = None                    ### Winding Edge Table      ###
        pSLL = None                     ### Current ScanLineList    ###
        ptsOut = None                   ### ptr to output buffers   ###
        #width
        FirstPoint = QList()
        FirstWidth = QList()
        for i in range(NUMPTSTOBUFFER):
            FirstPoint.append(DDXPointRec()) ### the output buffers ###
            FirstWidth.append(0)
        pPrevAET = None                 ### previous AET entry      ###
        ET = EdgeTable()                ### Edge Table header node  ###
        AET = EdgeTableEntry()          ### Active ET header node   ###
        pETEs = QList()                 ### Edge Table Entries buff ###
        SLLBlock = ScanLineListBlock()  ### header for ScanLineList ###
        fixWAET = 0
        if edges & Edge.Left.value:
            edge_l = 1
        else:
            edge_l = 0

        if edges & Edge.Right.value:
            edge_r = 1
        else:
            edge_r = 0

        if edges & Edge.Bottom.value:
            edge_b = 1
        else:
            edge_b = 0

        edge_t = 1 ##### (edges & Top) ? 1 : 0

        if (npoints == -1):
            npoints = pa.size()

        if (npoints < 3):
            return

        for i in range(npoints):
            pETEs.append(EdgeTableEntry())
        ptsOut = FirstPoint
        width = FirstWidth
        if (not miCreateETandAET(npoints, ptsIn, ET, AET, pETEs, SLLBlock)):
            del pETEs
            return
        pSLL = ET.scanlines.next

        if (not winding):
            ###
             #  for each scanline
            ###
            i = 0
            iwidth = 0
            for y in range(ET.ymin+1-edge_t, ET.ymax+edge_b):
                ###
                 #  Add a new edge to the active edge table when we
                 #  get to the next edge.
                ###
                if (pSLL and y == pSLL.scanline):
                    miloadAET(AET, pSLL.edgelist)
                    pSLL = pSLL.next
                pPrevAET = AET
                pAET = AET.next

                ###
                 #  for each active edge
                ###
                while (pAET):
                    ptsOut[i].x = pAET.bres.minor + 1 - edge_l
                    ptsOut[i].y = y
                    i += 1
                    width[iwidth] = pAET.next.bres.minor - pAET.bres.minor - 1 + edge_l + edge_r
                    iwidth += 1
                    nPts += 1

                    ###
                     #  send out the buffer when its full
                    ###
                    if (nPts == NUMPTSTOBUFFER):
                        self.processSpans(nPts, FirstPoint, FirstWidth)
                        i = 0
                        iwidth = 0
                        nPts = 0

                    pAET, pPrevAET = EVALUATEEDGEEVENODD(pAET, pPrevAET, y)
                    pAET, pPrevAET = EVALUATEEDGEEVENODD(pAET, pPrevAET, y)
                miInsertionSort(AET)
        else:      ### default to WindingNumber ###
            ###
             #  for each scanline
            ###
            i = 0
            for y in range(ET.ymin+1-edge_t, ET.ymax+edge_b):
                ###
                 #  Add a new edge to the active edge table when we
                 #  get to the next edge.
                ###
                if (pSLL and y == pSLL.scanline):
                    miloadAET(AET, pSLL.edgelist)
                    micomputeWAET(AET)
                    pSLL = pSLL.next
                pPrevAET = AET
                pAET = AET.next
                pWETE = pAET

                ###
                 #  for each active edge
                ###
                while (pAET):
                    ###
                    #  if the next edge in the active edge table is
                    #  also the next edge in the winding active edge
                    #  table.
                    ###
                    if (pWETE == pAET):
                        ptsOut[i].x = pAET.bres.minor + 1 - edge_l
                        ptsOut[i].y = y
                        i += 1
                        #width++ = pAET.nextWETE.bres.minor - pAET.bres.minor - 1 + edge_l + edge_r
                        nPts += 1

                        ###
                         #  send out the buffer
                        ###
                        if (nPts == NUMPTSTOBUFFER):
                            self.processSpans(nPts, FirstPoint, FirstWidth)
                            i = 0
                            iwidth = 0
                            nPts = 0

                        pWETE = pWETE.nextWETE
                        while (pWETE != pAET):
                            pAET, pPrevAET = EVALUATEEDGEWINDING(pAET, pPrevAET, y, fixWAET)
                        pWETE = pWETE.nextWETE
                    pAET, pPrevAET = EVALUATEEDGEWINDING(pAET, pPrevAET, y, fixWAET)

                ###
                #  reevaluate the Winding active edge table if we
                #  just had to resort it or if we just exited an edge.
                ###
                if (miInsertionSort(AET) or fixWAET):
                    micomputeWAET(AET)
                    fixWAET = 0

        ###
        #     Get any spans that we missed by buffering
        ###

        self.processSpans(nPts, FirstPoint, FirstWidth)
        miFreeStorage(SLLBlock.next)
###**** END OF X11-based CODE ****###

# Based on Xserver code miFillGeneralPoly...
###
# *
# *     Written by Brian Kelleher;  Oct. 1985
# *
# *     Routine to fill a polygon.  Two fill rules are
# *     supported: frWINDING and frEVENODD.
# *
# *     See fillpoly.h for a complete description of the algorithm.
# ###
#
###
#     These are the data structures needed to scan
#     convert regions.  Two different scan conversion
#     methods are available -- the even-odd method, and
#     the winding number method.
#     The even-odd rule states that a point is inside
#     the polygon if a ray drawn from that point in any
#     direction will pass through an odd number of
#     path segments.
#     By the winding number rule, a point is decided
#     to be inside the polygon if a ray drawn from that
#     point in any direction passes through a different
#     number of clockwise and counterclockwise path
#     segments.
#
#     These data structures are adapted somewhat from
#     the algorithm in (Foley/Van Dam) for scan converting
#     polygons.
#     The basic algorithm is to start at the top (smallest y)
#     of the polygon, stepping down to the bottom of
#     the polygon by incrementing the y coordinate.  We
#     keep a list of edges which the current scanline crosses, 
#     sorted by x.  This list is called the Active Edge Table (AET)
#     As we change the y-coordinate, we update each entry in
#     in the active edge table to reflect the edges new xcoord.
#     This list must be sorted at each scanline in case
#     two edges intersect.
#     We also keep a data structure known as the Edge Table (ET), 
#     which keeps track of all the edges which the current
#     scanline has not yet reached.  The ET is basically a
#     list of ScanLineList structures containing a list of
#     edges which are entered at a given scanline.  There is one
#     ScanLineList per scanline at which an edge is entered.
#     When we enter a new edge, we move it from the ET to the AET.
#
#     From the AET, we can implement the even-odd rule as in
#     (Foley/Van Dam).
#     The winding number rule is a little trickier.  We also
#     keep the EdgeTableEntries in the AET linked by the
#     nextWETE (winding EdgeTableEntry) link.  This allows
#     the edges to be linked just as before for updating
#     purposes, but only uses the edges linked by the nextWETE
#     link as edges representing spans of the polygon to
#     drawn (as with the even-odd rule).
###

### $XConsortium: miscanfill.h, v 1.5 94/04/17 20:27:50 dpw Exp $ ###
###
#
#Copyright (c) 1987  X Consortium
#
#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish, 
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be included
#in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#
#Except as contained in this notice, the name of the X Consortium shall
#not be used in advertising or otherwise to promote the sale, use or
#other dealings in this Software without prior written authorization
#from the X Consortium.
#
###

###
# *     scanfill.h
# *
# *     Written by Brian Kelleher; Jan 1985
# *
# *     This file contains a few macros to help track
# *     the edge of a filled object.  The object is assumed
# *     to be filled in scanline order, and thus the
# *     algorithm used is an extension of Bresenham's line
# *     drawing algorithm which assumes that y is always the
# *     major axis.
# *     Since these pieces of code are the same for any filled shape, 
# *     it is more convenient to gather the library in one
# *     place, but since these pieces of code are also in
# *     the inner loops of output primitives, procedure call
# *     overhead is out of the question.
# *     See the author for a derivation if needed.
# ###
#
###
#  In scan converting polygons, we want to choose those pixels
#  which are inside the polygon.  Thus, we add .5 to the starting
#  x coordinate for both left and right edges.  Now we choose the
#  first pixel which is inside the pgon for the left edge and the
#  first pixel which is outside the pgon for the right edge.
#  Draw the left pixel, but not the right.
#
#  How to add .5 to the starting x coordinate:
#      If the edge is moving to the right, then subtract dy from the
#  error term from the general form of the algorithm.
#      If the edge is moving to the left, then add dy to the error term.
#
#  The reason for the difference between edges moving to the left
#  and edges moving to the right is simple:  If an edge is moving
#  to the right, then we want the algorithm to flip immediately.
#  If it is moving to the left, then we don't want it to flip until
#  we traverse an entire pixel.
###

###
# *     This structure contains all of the information needed
# *     to run the bresenham algorithm.
# *     The variables may be hardcoded into the declarations
# *     instead of using this structure to make use of
# *     register declarations.
# ###
class BRESINFO():
    def __init__(self):
        self.minor = 0         ### minor axis        ###
        self.d = 0           ### decision variable ###
        self.m = self.m1 = 0       ### slope and slope+1 ###
        self.incr1 = self.incr2 = 0 ### error increments ###

def BRESINCRPGONSTRUCT(bres):
    if bres.m1 > 0:
        if (bres.d > 0):
            bres.minor += bres.m1
            bres.d += bres.incr1
        else:
            bres.minor += bres.m
            bres.d += bres.incr2
    else:
        if bres.d >= 0:
            bres.minor += bres.m1
            bres.d += bres.incr1
        else:
            bres.minor += bres.m
            bres.d += bres.incr2
    return bres

class EdgeTableEntry():
    def __init__(self):
        self.ymax = 0             ### ycoord at which we exit this edge. ###
        self.bres = BRESINFO()        ### Bresenham info to run the edge     ###
        self.next = None       ### next in the list     ###
        self.back = None       ### for insertion sort   ###
        self.nextWETE = None   ### for winding num rule ###
        self.ClockWise = 0        ### flag for winding number rule       ###

class ScanLineList():
    def __init__(self):
        self.scanline = 0              ### the scanline represented ###
        self.edgelist = None  ### header node              ###
        self.next = None  ### next in the list       ###

class EdgeTable():
    def __init__(self):
        self.ymax = 0                 ### ymax for the polygon     ###
        self.ymin = 0                 ### ymin for the polygon     ###
        self.scanlines = ScanLineList() ### header node              ###

###
# Here is a struct to help with storage allocation
# so we can allocate a big chunk at a time, and then take
# pieces from this heap when we need to.
###
SLLSPERBLOCK = 25

class ScanLineListBlock():
    def __init__(self):
        self.SLLs = QList()
        for i in range(SLLSPERBLOCK):
            self.SLLs.append(ScanLineList())
        self.next = None

###
# * number of points to buffer before sending them off
# * to scanlines() :  Must be an even number
# ###
NUMPTSTOBUFFER = 200
#
###
#
#     a few macros for the inner loops of the fill code where
#     performance considerations don't allow a procedure call.
#
#     Evaluate the given edge at the given scanline.
#     If the edge has expired, then we leave it and fix up
#     the active edge table; otherwise, we increment the
#     x value to be ready for the next scanline.
#     The winding number rule is in effect, so we must notify
#     the caller when the edge has been removed so he
#     can reorder the Winding Active Edge Table.
###
def EVALUATEEDGEWINDING(pAET, pPrevAET, y, fixWAET=1):
    if pAET.ymax == y:          ## leaving this edge ##
        pPrevAET.next = pAET.next
        pAET = pPrevAET.next
        #fixWAET = 1
        if pAET:
            pAET.back = pPrevAET
    else:
        BRESINCRPGONSTRUCT(pAET.bres)
        pPrevAET = pAET
        pAET = pAET.next
    return (pAET, pPrevAET)

###
# *     Evaluate the given edge at the given scanline.
# *     If the edge has expired, then we leave it and fix up
# *     the active edge table; otherwise, we increment the
# *     x value to be ready for the next scanline.
# *     The even-odd rule is in effect.
# ###
def EVALUATEEDGEEVENODD(pAET, pPrevAET, y):
    if pAET:
        if (pAET.ymax == y):          ### leaving this edge ### 
            pPrevAET.next = pAET.next
            pAET = pPrevAET.next
            if pAET:
                pAET.back = pPrevAET
        else:
            pAET.bres = BRESINCRPGONSTRUCT(pAET.bres)
            pPrevAET = pAET
            pAET = pAET.next
    return pAET, pPrevAET

##############################################################
#
#Copyright (c) 1987  X Consortium
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
#X CONSORTIUM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
#AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#Except as contained in this notice, the name of the X Consortium shall not be
#used in advertising or otherwise to promote the sale, use or other dealings
#in this Software without prior written authorization from the X Consortium.
#
#
#Copyright 1987 by Digital Equipment Corporation, Maynard, Massachusetts.
#
#                        All Rights Reserved
#
#Permission to use, copy, modify, and distribute this software and its
#documentation for any purpose and without fee is hereby granted, 
#provided that the above copyright notice appear in all copies and that
#both that copyright notice and this permission notice appear in
#supporting documentation, and that the name of Digital not be
#used in advertising or publicity pertaining to distribution of the
#software without specific, written prior permission.
#
#DIGITAL DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
#ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL
#DIGITAL BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
#ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, 
#WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, 
#ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
#SOFTWARE.
#
###***************************************************************###
#
MAXINT = 0x7fffffff
MININT = -MAXINT
#
###
#       fillUtils.c
#
#       Written by Brian Kelleher;  Oct. 1985
#
#       This module contains all of the utility functions
#       needed to scan convert a polygon.
#
###
###
# *     InsertEdgeInET
# *
# *     Insert the given edge into the edge table.
# *     First we must find the correct bucket in the
# *     Edge table, then find the right slot in the
# *     bucket.  Finally, we can insert it.
# *
# ###
def miInsertEdgeInET(ET, ETE, scanline, SLLBlock, iSLLBlock):
    ###
    # find the right bucket to put the edge into
    ###
    pPrevSLL = ET.scanlines
    pSLL = pPrevSLL.next
    while (pSLL and (pSLL.scanline < scanline)):
        pPrevSLL = pSLL
        pSLL = pSLL.next

    ###
    # reassign pSLL (pointer to ScanLineList) if necessary
    ###
    if ((not pSLL) or (pSLL.scanline > scanline)):
        if (iSLLBlock > SLLSPERBLOCK-1):
            tmpSLLBlock = ScanLineListBlock()
            if (not tmpSLLBlock):
                return -1
            SLLBlock.next = tmpSLLBlock
            tmpSLLBlock.next = 0
            SLLBlock = tmpSLLBlock
            iSLLBlock = 0
        pSLL = SLLBlock.SLLs[iSLLBlock]
        iSLLBlock += 1
        pSLL.next = pPrevSLL.next
        pSLL.edgelist = 0
        pPrevSLL.next = pSLL
    pSLL.scanline = scanline

    ###
    # now insert the edge in the right bucket
    ###
    prev = 0
    start = pSLL.edgelist
    while (start and (start.bres.minor < ETE.bres.minor)):
        prev = start
        start = start.next
    ETE.next = start

    if (prev):
        prev.next = ETE
    else:
        pSLL.edgelist = ETE
    return iSLLBlock

###
#     CreateEdgeTable
#
#     This routine creates the edge table for
#     scan converting polygons.
#     The Edge Table (ET) looks like:
#
#    EdgeTable
#     --------
#    |  ymax  |        ScanLineLists
#    |scanline|-.-----------.-------------....
#     --------   |scanline|   |scanline|
#                |edgelist|   |edgelist|
#                ---------    ---------
#                    |             |
#                    |             |
#                    V             V
#              list of ETEs   list of ETEs
#
#     where ETE is an EdgeTableEntry data structure, 
#     and there is one ScanLineList per scanline at
#     which an edge is initially entered.
#
###
class DDXPointRec():
    def __init__(self):
        self.x = self.y = 0

###
# *     Clean up our act.
# ###
def miFreeStorage(pSLLBlock):
    while pSLLBlock:
        tmpSLLBlock = pSLLBlock.next
        del pSLLBlock
        pSLLBlock = tmpSLLBlock
    del pSLLBlock

def BRESINITPGONSTRUCT(dy, x1, x2, bres):
    dx = 0      # local storage #
    ###
    #  if the edge is horizontal, then it is ignored 
    #  and assumed not to be processed.  Otherwise, do this stuff. 
    ###
    if dy != 0:
        bres.minor = x1
        dx = x2 - bres.minor
        if dx < 0:
            bres.m = int(dx / dy)
            bres.m1 = bres.m - 1
            bres.incr1 = -2 * dx + 2 * dy * bres.m1
            bres.incr2 = -2 * dx + 2 * dy * bres.m
            bres.d = 2 * bres.m * dy - 2 * dx - 2 * dy
        else:
            bres.m = int(dx / dy)
            bres.m1 = bres.m + 1
            bres.incr1 = 2 * dx - 2 * dy * bres.m1
            bres.incr2 = 2 * dx - 2 * dy * bres.m
            bres.d = -2 * bres.m * dy + 2 * dx
    return bres

def miCreateETandAET(count, pts, ET, AET, pETEs, pSLLBlock):
    iSLLBlock = 0

    if count < 2:
        return True

    ###
    #  initialize the Active Edge Table
    ###
    AET.next = 0
    AET.back = 0
    AET.nextWETE = 0
    AET.bres.minor = MININT

    ###
    #  initialize the Edge Table.
    ###
    ET.scanlines.next = 0
    ET.ymax = MININT
    ET.ymin = MAXINT
    pSLLBlock.next = 0

    PrevPt = pts[-1]

    ###
    #  for each vertex in the array of points.
    #  In this loop we are dealing with two vertices at
    #  a time -- these make up one edge of the polygon.
    ###
    i = 0
    j = 0
    while (count):
        CurrPt = pts[i]
        i += 1

        ###
        #  find out which point is above and which is below.
        ###
        if (PrevPt.y() > CurrPt.y()):
            bottom = PrevPt
            top = CurrPt
            pETEs[j].ClockWise = 0
        else:
            bottom = CurrPt
            top = PrevPt
            pETEs[j].ClockWise = 1

        ###
        # don't add horizontal edges to the Edge table.
        ###
        if (bottom.y() != top.y()):
            pETEs[j].ymax = bottom.y()-1;  ### -1 so we don't get last scanline ###

            ###
            #  initialize integer edge algorithm
            ###
            dy = bottom.y() - top.y()
            BRESINITPGONSTRUCT(dy, top.x(), bottom.x(), pETEs[j].bres)
            iSLLBlock = miInsertEdgeInET(ET, pETEs[j], top.y(), pSLLBlock, iSLLBlock)
            if iSLLBlock==-1:
                miFreeStorage(pSLLBlock.next)
                return False

            ET.ymax = max(ET.ymax, PrevPt.y())
            ET.ymin = min(ET.ymin, PrevPt.y())
            j += 1

        PrevPt = CurrPt
        count -= 1
    return True

###
#     loadAET
#
#     This routine moves EdgeTableEntries from the
#     EdgeTable into the Active Edge Table, 
#     leaving them sorted by smaller x coordinate.
#
###
def miloadAET(AET, ETEs):
    pPrevAET = AET
    AET = AET.next
    while (ETEs):
        while (AET and (AET.bres.minor < ETEs.bres.minor)):
            pPrevAET = AET
            AET = AET.next
        tmp = ETEs.next
        ETEs.next = AET
        if (AET):
            AET.back = ETEs
        ETEs.back = pPrevAET
        pPrevAET.next = ETEs
        pPrevAET = ETEs

        ETEs = tmp

###
# *     computeWAET
# *
# *     This routine links the AET by the
# *     nextWETE (winding EdgeTableEntry) link for
# *     use by the winding number rule.  The final
# *     Active Edge Table (AET) might look something
# *     like:
# *
# *     AET
# *     ----------  ---------   ---------
# *     |ymax    |  |ymax    |  |ymax    |
# *     | ...    |  |...     |  |...     |
# *     |next    |.|next    |.|next    |....
# *     |nextWETE|  |nextWETE|  |nextWETE|
# *     ---------   ---------   ^--------
# *         |                   |       |
# *         V------------------.       V--. ...
# *
# ###
def micomputeWAET(AET):
    inside = 1
    isInside = 0

    AET.nextWETE = 0
    pWETE = AET
    AET = AET.next
    while (AET):
        if (AET.ClockWise):
            isInside += 1
        else:
            isInside -= 1

        if ((not inside and not isInside) or (inside and  isInside)):
            pWETE.nextWETE = AET
            pWETE = AET
            inside = not inside
        AET = AET.next
    pWETE.nextWETE = 0

###
#     InsertionSort
#
#     Just a simple insertion sort using
#     pointers and back pointers to sort the Active
#     Edge Table.
#
###
def miInsertionSort(AET):
    changed = 0

    AET = AET.next
    while (AET):
        pETEinsert = AET
        pETEchase = AET
        while (pETEchase.back.bres.minor > AET.bres.minor):
            pETEchase = pETEchase.back

        AET = AET.next
        if (pETEchase != pETEinsert):
            pETEchaseBackTMP = pETEchase.back
            pETEinsert.back.next = AET
            if (AET):
                AET.back = pETEinsert.back
            pETEinsert.next = pETEchase
            pETEchase.back.next = pETEinsert
            pETEchase.back = pETEinsert
            pETEinsert.back = pETEchaseBackTMP
            changed = 1
    return changed

class QtCanvasPolygonScanner(QtPolygonScanner):
    def __init__(self, p):
        self.processor = p

    def processSpans(self, n, point, width):
        self.processor.doSpans(n, point, width)
