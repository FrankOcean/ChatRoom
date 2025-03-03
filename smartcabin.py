from PyQt5 import QtWidgets
from mainwindow.main_window import Ui_MainWindow
from smart_derain import SmartDerainWindow
from dehaze.dehaze import Ui_DehazeForm
from eye_track.smart_eyetrack import SmartEyetrackWindow
from face_rec.smart_facerec import SmartFaceWindow
from gesture_rec.gesture import Ui_GestureForm
from semantic_seg.semantic import Ui_SemanticForm
from imglink.imglink import Ui_ImglinkForm
# 系统主菜单
class SmartWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(SmartWindow, self).__init__()
        self.setupUi(self)

        self.actionderain.triggered.connect(self.open_derain_window)
        self.actiondehaze.triggered.connect(self.open_dehaze_window)
        self.actionfacerec.triggered.connect(self.open_facerec_window)
        self.actionimglink.triggered.connect(self.open_imglink_window)
        self.actiongesture.triggered.connect(self.open_gesturerec_window)
        self.actioneyetrack.triggered.connect(self.open_eyetrack_window)
        self.actionsemantic.triggered.connect(self.open_segmentic_window)

    def hide_banner(self):
        self.banner1.hide()
        self.banner2.hide()
        self.verticalLayout.removeWidget(self.child)

    # 打开去雨窗口
    def open_derain_window(self):
        self.child = SmartDerainWindow()
        self.verticalLayout.addWidget(self.child)
        self.hide_banner()
        self.child.show()

    # 打开去尘窗口
    def open_dehaze_window(self):
        self.child = ChildrenDehazeForm()
        self.verticalLayout.addWidget(self.child)
        self.child.show()
        self.hide_banner()

    # 打开眼动窗口
    def open_eyetrack_window(self):
        self.child = SmartEyetrackWindow()
        self.verticalLayout.addWidget(self.child)
        self.hide_banner()
        self.child.show()

    # 打开人脸识别窗口
    def open_facerec_window(self):
        self.child = SmartFaceWindow()
        self.verticalLayout.addWidget(self.child)
        self.hide_banner()
        self.child.show()

    # 打开手势识别窗口
    def open_gesturerec_window(self):
        self.child = ChildrenGestureForm()
        self.verticalLayout.addWidget(self.child)
        self.child.show()
        self.hide_banner()

    # 打开语义分割窗口
    def open_segmentic_window(self):
        self.child = ChildrenSemanticForm()
        self.verticalLayout.addWidget(self.child)
        self.child.show()
        self.hide_banner()

    # 打开语义分割窗口
    def open_imglink_window(self):
        self.child = ChildrenImglinkForm()
        self.verticalLayout.addWidget(self.child)
        self.child.show()
        self.hide_banner()

    # 测试事件
    def testClick(self):
        self.msg()

    def msg(self):
        QtWidgets.QMessageBox.information(self,  # 使用infomation信息框
                                        "标题",
                                        "测试用",
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)


# 2. dehaze children window
class ChildrenDehazeForm(QtWidgets.QWidget, Ui_DehazeForm):
    def __init__(self):
        super(ChildrenDehazeForm, self).__init__()
        self.setupUi(self)

# 4. gesture recognition children window
class ChildrenGestureForm(QtWidgets.QWidget, Ui_GestureForm):
    def __init__(self):
        super(ChildrenGestureForm, self).__init__()
        self.setupUi(self)

# 5. semantic segmentition window
class ChildrenSemanticForm(QtWidgets.QWidget, Ui_SemanticForm):
    def __init__(self):
        super(ChildrenSemanticForm, self).__init__()
        self.setupUi(self)

# 7. image link children window
class ChildrenImglinkForm(QtWidgets.QWidget, Ui_ImglinkForm):
    def __init__(self):
        super(ChildrenImglinkForm, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    smart = SmartWindow()
    smart.show()
    sys.exit(app.exec_())