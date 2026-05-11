"""
ZP Stage Controller
Handles Zone Plate (ZP) microscope stage movements and controls

This module provides methods for:
- Sample stage movements (SMAR-X, SMAR-Y, SMAR-Z)
- ZP theta rotation stage
- ZP Z-axis (ZPZ1) focusing stage
- OSA (Order Sorting Aperture) positioning
- Beamstop (BS) positioning
- Configuration presets (cam11 view, nanobeam mode)
"""

from qtpy import QtTest
from utilities import show_error_message_box, with_motion_feedback
from epics import caput


class ZPStageController:
    """Mixin class for ZP stage control functionality"""
    
    def connect_zp_stages(self):
        """Connect ZP stage UI signals to control methods"""
        # ZP navigation - positive direction buttons
        self.pb_move_smarx_pos.clicked.connect(lambda: self.move_smarx())
        self.pb_move_smary_pos.clicked.connect(lambda: self.move_smary())
        self.pb_move_smarz_pos.clicked.connect(lambda: self.move_smarz())
        self.pb_move_zpsth_pos.clicked.connect(lambda: self.move_zpth())
        self.pb_move_zpz_pos.clicked.connect(lambda: self.move_zpz1())

        # ZP navigation - negative direction buttons
        self.pb_move_smarx_neg.clicked.connect(lambda: self.move_smarx(neg_=True))
        self.pb_move_smary_neg.clicked.connect(lambda: self.move_smary(neg_=True))
        self.pb_move_smarz_neg.clicked.connect(lambda: self.move_smarz(neg_=True))
        self.pb_move_zpsth_pos_neg.clicked.connect(lambda: self.move_zpth(neg_=True))
        self.pb_move_zpz_neg.clicked.connect(lambda: self.move_zpz1(neg_=True))
        
        # Stop all motion button
        self.pb_zp_stop_all_sample.clicked.connect(lambda: stop_all_zp_motion())

    # ========== Sample Stage Movements ==========
    
    def move_smarx(self, neg_=False):
        """Move SMAR-X stage (horizontal sample position)"""
        self.moveAMotor(self.db_move_smarx, smarx, 1, neg=neg_)

    def move_smary(self, neg_=False):
        """Move SMAR-Y stage (vertical sample position)"""
        self.moveAMotor(self.db_move_smary, smary, 1, neg=neg_)

    def move_smarz(self, neg_=False):
        """Move SMAR-Z stage (depth sample position)"""
        self.moveAMotor(self.db_move_smarz, smarz, 1, neg=neg_)

    def move_zpth(self, neg_=False):
        """Move ZP theta rotation stage"""
        self.moveAMotor(self.db_move_zpsth, zpsth, neg=neg_)

    def move_zpz1(self, neg_=False):
        """Move ZP Z1 focusing stage"""
        if neg_:
            RE(movr_zpz1(self.db_move_zpz.value() * 0.001 * -1))
        else:
            RE(movr_zpz1(self.db_move_zpz.value() * 0.001))

    # ========== Configuration Preset Methods ==========
    
    @show_error_message_box
    @with_motion_feedback(title="ZP to cam 11", success_msg="ZP microscope is ready for cam11 view.")
    def zp_to_cam11_view_(self):
        """Move ZP microscope to cam11 viewing configuration"""
        RE(zp_to_cam11_view())

    @show_error_message_box
    @with_motion_feedback(title="ZP to nanobeam", success_msg="ZP microscope is ready for nanobeam.")
    def zp_to_nanobeam_(self):
        """Move ZP microscope to nanobeam measurement configuration"""
        RE(zp_to_nanobeam())

    # ========== OSA (Order Sorting Aperture) Control ==========
    
    @show_error_message_box
    @with_motion_feedback(title="ZP OSA Move", success_msg="ZP OSA Y moved OUT.")
    def ZP_OSA_OUT(self):
        """Move ZP Order Sorting Aperture OUT of beam"""
        RE(zp_osa_out())
        self.statusbar.showMessage('OSA Y moved OUT')

    @show_error_message_box
    @with_motion_feedback(title="ZP OSA Move", success_msg="ZP OSA Y moved IN.")
    def ZP_OSA_IN(self):
        """Move ZP Order Sorting Aperture INTO beam"""
        RE(zp_osa_in())
        self.statusbar.showMessage('OSA Y IN')

    # ========== Beamstop Control ==========
    
    @with_motion_feedback(title="ZP BSY Move", success_msg="ZP BSY motion completed.")
    @show_error_message_box
    def ZP_BS_OUT(self):
        """Move ZP beamstop OUT of beam"""
        RE(zp_bs_out())
        self.statusbar.showMessage('BS Y moved OUT')

    @with_motion_feedback(title="ZP BSY Move", success_msg="ZP BSY motion completed.")
    @show_error_message_box
    def ZP_BS_IN(self):
        """Move ZP beamstop INTO beam"""
        RE(zp_bs_in())
        self.statusbar.showMessage('BS Y moved in')
