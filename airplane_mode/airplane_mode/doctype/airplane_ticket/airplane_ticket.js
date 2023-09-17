// Copyright (c) 2023, scopen.fr and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
  refresh: function (frm) {
    frm.add_custom_button(__('Assign Seat'), function () {
      let d = new frappe.ui.Dialog({
        title: 'Select Seat',
        fields: [
          {
            label: __('Seat Number'),
            fieldname: 'seat_number',
            fieldtype: 'Data',
          },
        ],
        size: 'small', // small, large, extra-large
        primary_action_label: __('Assign'),
        primary_action(values) {
          frm.set_value('seat',values.seat_number);
          d.hide();
        }
      });
      d.show();
    }, __("Actions"));
  }

});
