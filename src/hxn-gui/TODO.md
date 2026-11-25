# HXN GUI TODO

Bugs found while writing tooltips ([tooltips.json](tooltips.json)). When you fix an item, update the tooltips of the widgets involved so they no longer warn about it, then remove the item here.

## Confirmation ignored

- [ ] `copy_data_to_globus` (`pb_move_data_to_globus`) and `move_energy_with_sid_gui` (`pb_energy_change_w_sid`) use `if QMessageBox.Yes:`, which is always true, so they run even when the user clicks No. Use `if choice == QMessageBox.Yes:`.

## Crashes and errors

- [ ] `pb_laser_in` calls `self.cam06_laser_in`, which does not exist. Use `self.cam6LASER` (as the Energy tab does).
- [ ] `pb_center_ssa2_auto` calls `RE(self.center_ssa2())`; `center_ssa2` is a startup plan, not a GUI method. Use `RE(center_ssa2())`.
- [ ] `pb_merlin_filterIN/OUT` wrap `toggle_merlin_filter` in `RE(...)`, but it is a plain function, not a plan: the filter moves, then `RE` raises. Call it directly.

## Unsafe

- [ ] `pb_mll_z_focus_move` always moves `sbz` without confirmation, ignoring `cb_mll_z_motor_move`. Use the selected motor and confirm.

## Wrong labels

- [ ] ZP optics: `pb_osa_in` "OSA IN (Y+2700)" moves -2700 and `pb_osa_out` moves +2700; `pb_zpbsy_in/out` move -100/+100. Fix the signs in the button text.

## Input and features

- [ ] `le_plot_sd` only accepts integers (`only_int_le`), but `plot_me` supports a range like `100,110`. Relax the validator.

## Buttons not connected

- [ ] Alignment: `pb_zp_rot_move_smarx`, `pb_zp_rot_move_smarz`, `pb_zp_rot_rotate_to`, `pb_rot_align_dsth/dsx/dsz/sbx_move`, `pb_rot_align_all_move`, `pb_stop_mll_motion`.
- [ ] Detectors: `pb_telescope`, `pb_abort_diff`, `pb_flatfield_save_enable`, `pb_flatfield_disable` (flat field for `cb_dets_for_ff_corr`), `pb_eiger_filter_a/b/c_in/out`, all `gb_attenuators` buttons (`*_2`).
- [ ] Other: `pb_roiList_clear_sel_mll/zp`, `pb_insert_user_image`, `pb_engage_mirror_feedbacks`.

## Profile startup files (hxn-profile-collection)

- [ ] `72-json-plans.py` `run_diff_json` passes `xalign/yalign["center_with"]` as `align_scan`'s `line_center_mode`; pass `["line_center_mode"]` so the Diffraction tab setting takes effect.
- [ ] `run_diff_json` does not read `custom_angle_list`; the GUI summary assumes it replaces start/end/step.
- [ ] `run_tomo_json` does not read `align_using_previous`; the Tomography group is only saved to the JSON.

## Beamline setup

- [ ] `run-queue-server` must start the RE Manager with `--zmq-publish-console ON`, then restart QServer; otherwise the QServer Console tab stays empty.
- [ ] ROI Planner tab: check image orientation on a real scan. XRF maps have appeared flipped before, which moves ROI coordinates. The planner uses `axisOrder="row-major"` on its own image (the global pyqtgraph setting is only changed when run standalone); the live Tomo/Diff viewers use the default column-major order and transpose. Mark an ROI on a known feature, send the plan, and confirm the fine scan lands on it; compare with the same scan in the live viewer.
