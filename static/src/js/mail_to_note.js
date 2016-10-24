openerp.mail_to_note = function(openerp) {
    var _t = openerp.web._t;
    var initial_mode = "view"
    var QWeb = openerp.web.qweb;

    openerp.mail.ThreadMessage.include({
        bind_events: function () {
            var self = this;
            this._super();
            this.$el.find('.oe_msg_create_note').on('click', this.on_create_note);
        },
        on_create_note: function (default_composition_mode) {
            var self = this
            messages = []
            attachment_ids = []
            var msg = false
            _.each(self.attachment_ids, function (attachment) {
                    attachment_ids.push(attachment.id)
            });
            var values = new openerp.web.Model('mail.message').call('create_note', [[this.id]])
            values.done(function(vals) {
                console.log("valsvalsvalsvalsvals",vals)
            })
        },
    })
};
