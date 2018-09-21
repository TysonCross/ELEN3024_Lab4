#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Sep 21 15:43:15 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

def struct(data): return type('Struct', (object,), data)()
from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 702
        self.freq_adjust_fine = freq_adjust_fine = 0
        self.freq_adjust_coarse = freq_adjust_coarse = 0
        self.volume = volume = .5
        self.variable_struct_0 = variable_struct_0 = struct({'field0': 0, })
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = variable_qtgui_chooser_0
        self.samp_rate = samp_rate = 64e3
        self.resamp_factor = resamp_factor = 4
        self.freq_base = freq_base = 1069.25e3
        self.freq_adjust_0 = freq_adjust_0 = variable_qtgui_chooser_0
        self.freq_adjust = freq_adjust = (freq_adjust_coarse*1e6)+ (freq_adjust_fine*1e3)

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 1, 0.1, .5, 50)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: repr(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Test'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 5, 1, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_chooser_0_options = (702, 1485, 2000, )
        self._variable_qtgui_chooser_0_labels = ('LM', 'Veritas', 'Test', )
        self._variable_qtgui_chooser_0_group_box = Qt.QGroupBox('Choose Station')
        self._variable_qtgui_chooser_0_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_qtgui_chooser_0_button_group = variable_chooser_button_group()
        self._variable_qtgui_chooser_0_group_box.setLayout(self._variable_qtgui_chooser_0_box)
        for i, label in enumerate(self._variable_qtgui_chooser_0_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._variable_qtgui_chooser_0_box.addWidget(radio_button)
        	self._variable_qtgui_chooser_0_button_group.addButton(radio_button, i)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_button_group.buttonClicked[int].connect(
        	lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_0_group_box, 5, 3, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=64,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	20e6, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 3, 1, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	1.6e6, #bw
        	"Raw Signal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 4, 1, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Adjusted Input Signal", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 4, 2, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(resamp_factor, firdes.low_pass(
        	1, samp_rate, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self._freq_adjust_fine_range = Range(-5.0, 5.0, 0.5, 0, 50)
        self._freq_adjust_fine_win = RangeWidget(self._freq_adjust_fine_range, self.set_freq_adjust_fine, 'Adjust Frequency kHz', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_adjust_fine_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_adjust_coarse_range = Range(-10.0, 10.0, 0.1, 0, 50)
        self._freq_adjust_coarse_win = RangeWidget(self._freq_adjust_coarse_range, self.set_freq_adjust_coarse, 'Adjust Frequency MHz', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_adjust_coarse_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/Users/Tyson/Documents/Academic/ELEN3024/GNURadio Tutorials/am_usrp710.dat', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_adjust, 1, 0)
        self.analog_agc2_xx_0 = analog.agc2_cc(6.25e-4, 1e-5, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.audio_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.variable_qtgui_chooser_0))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.set_freq_adjust_0(self.variable_qtgui_chooser_0)

    def get_freq_adjust_fine(self):
        return self.freq_adjust_fine

    def set_freq_adjust_fine(self, freq_adjust_fine):
        self.freq_adjust_fine = freq_adjust_fine
        self.set_freq_adjust((self.freq_adjust_coarse*1e6)+ (self.freq_adjust_fine*1e3))

    def get_freq_adjust_coarse(self):
        return self.freq_adjust_coarse

    def set_freq_adjust_coarse(self, freq_adjust_coarse):
        self.freq_adjust_coarse = freq_adjust_coarse
        self.set_freq_adjust((self.freq_adjust_coarse*1e6)+ (self.freq_adjust_fine*1e3))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_variable_struct_0(self):
        return self.variable_struct_0

    def set_variable_struct_0(self, variable_struct_0):
        self.variable_struct_0 = variable_struct_0

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_resamp_factor(self):
        return self.resamp_factor

    def set_resamp_factor(self, resamp_factor):
        self.resamp_factor = resamp_factor

    def get_freq_base(self):
        return self.freq_base

    def set_freq_base(self, freq_base):
        self.freq_base = freq_base

    def get_freq_adjust_0(self):
        return self.freq_adjust_0

    def set_freq_adjust_0(self, freq_adjust_0):
        self.freq_adjust_0 = freq_adjust_0

    def get_freq_adjust(self):
        return self.freq_adjust

    def set_freq_adjust(self, freq_adjust):
        self.freq_adjust = freq_adjust
        self.analog_sig_source_x_0.set_frequency(self.freq_adjust)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
