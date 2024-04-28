from database import db
from database.models.tax_information import TaxInformation


class TaxInformationRepository:
    def add_tax_information(self, tax_info_data, flush=False):
        tax_information = TaxInformation(**tax_info_data)
        db.session.add(tax_information)
        if flush:
            db.session.flush()
        else:
            db.session.commit()
        return tax_information

    def get_tax_information_by_id(self, tax_info_id):
        return TaxInformation.query.filter_by(id=tax_info_id).first()

    def update_tax_information(self, tax_info_id, update_data):
        tax_information = self.get_tax_information_by_id(tax_info_id)
        if tax_information:
            for key, value in update_data.items():
                setattr(tax_information, key, value)
            db.session.commit()
        return tax_information

    def delete_tax_information(self, tax_info_id):
        tax_information = self.get_tax_information_by_id(tax_info_id)
        if tax_information:
            db.session.delete(tax_information)
            db.session.commit()
        return tax_information
