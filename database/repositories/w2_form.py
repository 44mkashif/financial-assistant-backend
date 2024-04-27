from database import db
from database.models.w2_form import W2Form

class W2FormRepository:
    def add_w2_form(self, w2_form_data, flush=False):
        w2_form = W2Form(**w2_form_data)
        db.session.add(w2_form)
        if flush:
            db.session.flush()
        else:
            db.session.commit()
        return w2_form

    def get_w2_form_by_id(self, w2_form_id):
        return W2Form.query.filter_by(id=w2_form_id).first()

    def update_w2_form(self, w2_form_id, update_data):
        w2_form = self.get_w2_form_by_id(w2_form_id)
        if w2_form:
            for key, value in update_data.items():
                setattr(w2_form, key, value)
            db.session.commit()
        return w2_form

    def delete_w2_form(self, w2_form_id):
        w2_form = self.get_w2_form_by_id(w2_form_id)
        if w2_form:
            db.session.delete(w2_form)
            db.session.commit()
        return w2_form
