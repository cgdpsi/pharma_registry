FROM odoo:16.0

USER root
RUN pip3 install --no-cache-dir openpyxl xlsxwriter
COPY ./custom_addons /mnt/extra-addons
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo
COPY ./odoo.conf /etc/odoo/odoo.conf
