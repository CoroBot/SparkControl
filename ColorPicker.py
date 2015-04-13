from PySide import QtCore, QtGui
import math

def _draw_cherckerboard(painter, rect, size):
    color1 = QtGui.QColor(153, 153, 152)
    color2 = QtGui.QColor(102, 102, 102)

    painter.save()
    painter.fillRect(rect, color1)
    square = QtCore.QRect(0,0,size,size)
    step_x = size*2
    step_y = size
    odd = True

    while square.top() < rect.bottom():
        while square.left() < rect.right():
            painter.fillRect(square, color2)
            square.moveLeft(squre.left() + step_x)
        square.moveLeft(0)

        if odd:
            square.moveLeft(square.left() + step_x / 2.0)
        square.moveTop(square.top() + step_y) 
        odd = not odd
    painter.restore

    class ColorWidget(QtGui.QWidget)
        """
        Base class for widgets manipulating colors.
        """
        colorChanged = QtCore.Signal(QtGui.QColor)
        '''
        Emitted when the color has changed. Contains a matching QColor.
        '''

        def __init__(self, parent=None):
            super(ColorWidget, self).__init__(parent)

            self._color = QtGui.QColor()

        def color(self):
            '''
            The QColor represented by this widget.
            :return: A selected color
            :return type: QColor (Typically in RGB?)
            '''

            return QtGui.QColor(self._color)

        def updateColor(self, color):
            '''
            Updates the color represented by this widget. Does not emite a
            signal.
            :parameter color: The new selected color
            :type color: QColor
            '''

            self._color = QtGui.QColor(color)
            self.repaint()

        def setColor(self, color):


