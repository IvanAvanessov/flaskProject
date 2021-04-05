from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify
from datetime import datetime
import random

ccyapp_url = Blueprint('ccyapp', __name__, template_folder='templates')


@ccyapp_url.route('/<ccypair>', methods=['GET'])
def get_ccy_rate_for(ccypair):
    return round(random.uniform(1, 1.3), 4)
