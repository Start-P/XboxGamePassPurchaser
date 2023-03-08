import requests
import random
import re

from tools import tools

class UnsupportedCard(Exception):
    """Unsupported Card Type Error"""


prePareCartFlights = ['sc_appendconversiontype', 'sc_showvalidpis', 'sc_scdstextdirection', 'sc_optimizecheckoutload', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_showcanceldisclaimerdefaultv1', 'sc_redirecttosignin', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_promocode', 'sc_onedrivedowngrade', 'sc_newooslogiconcart', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_hidecontactcheckbox', 'sc_preparecheckoutrefactor', 'sc_checkoutklarna', 'sc_currencyformattingpkg', 'sc_fullpageredirectionforasyncpi', 'sc_xaaconversionerror', 'sc_promocodefeature-web-desktop', 'sc_eligibilityproducts', 'sc_disabledpaymentoption',
                      'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_dynamicseligibility', 'sc_usebuynowonlyinternalendpoint', 'sc_removemoreless', 'sc_renewalsubscriptionselector', 'sc_hidexdledd', 'sc_militaryshippingurl', 'sc_xboxdualleaf', 'sc_japanlegalterms', 'sc_multiplesubscriptions', 'sc_loweroriginalprice', 'sc_xaatovalenciastring', 'sc_cannotbuywarrantyalone', 'sc_showminimalfooteroncheckout', 'sc_checkoutdowngrade', 'sc_checkoutcontainsiaps', 'sc_localizedtax', 'sc_officescds', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_checkoutscenariotelemetry', 'sc_skipselectpi', 'sc_allowmpesapi', 'sc_purchasestatusmessage', 'sc_storetermslink', 'sc_postorderinfolineitemmessage', 'sc_addpaymentfingerprinttagging', 'sc_shippingallowlist', 'sc_emptyresultcheck', 'sc_dualleaf', 'sc_riskyxtoken', 'sc_abandonedretry', 'sc_testflightbuynow', 'sc_addshippingmethodtelemetry', 'sc_leaficons', 'sc_newspinneroverlay', 'sc_paymentinstrumenttypeandfamily', 'sc_addsitename', 'sc_disallowalipayforcheckout', 'sc_checkoutsignintelemetry', 'sc_prominenteddchange', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf',
                      'sc_buynowctatext', 'sc_buynowuiprod', 'sc_checkoutsalelegaltermsjp', 'sc_showooserrorforoneminute', 'sc_proratedrefunds', 'sc_entitlementcheckallitems', 'sc_indiaregsbanner', 'sc_checkoutentitlement', 'sc_rspv2', 'sc_focustrapforgiftthankyoupage', 'sc_hideneedhelp', 'sc_defaultshippingref', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_nativeclientlinkredirect', 'sc_enablelegalrequirements', 'sc_expanded.purchasespinner', 'sc_valenciaupgrade', 'sc_enablezipplusfour', 'sc_giftingtelemetryfix', 'sc_handleentitlementerror', 'sc_alwayscartmuid', 'sc_sharedupgrade', 'sc_checkoutloadspinner', 'sc_xaaconversionexpirationdate', 'sc_helptypescript', 'sc_newdemandsandneedsstatement', 'sc_citizensoneallowed', 'sc_riskfatal', 'sc_renewtreatmenta', 'sc_trialtreatmenta', 'sc_cartzoomfix', 'sc_useofficeonlyinternalendpoint', 'sc_gotopurchase', 'sc_endallactivities', 'sc_headingheader', 'sc_flexsubs', 'sc_useanchorcomponent', 'sc_addbillingaddresstelemetry', 'sc_replacestoreappclient', 'sc_scenariotelemetryrefactor', 'sc_checkoutsmd', 'sc_scenariosupportupdate', 'sc_bankchallengecheckout', 'sc_addpaymenttelemetry', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_xboxgotocart', 'sc_hidewarningevents', 'sc_xboxcomnosapi', 'sc_routebacktocartforoutofstock', 'sc_clientdebuginfo', 'sc_koreanlegalterms', 'sc_refactorprorate', 'sc_paymentoptionnotfound', 'sc_pidlflights', 'sc_fixcolorcontrastforrecommendeditems', 'sc_hideeditbuttonwhenediting', 'sc_enablekakaopay', 'sc_ordercheckoutfix', 'sc_xboxpmgrouping', 'sc_stickyfooter', 'sc_gotoredmrepl', 'sc_partnernametelemetry', 'sc_jpregionconversion', 'sc_checkoutorderedpv', 'sc_maxaddresslinelength', 'sc_componentexception', 'sc_buynowuipreload', 'sc_updatebillinginfo', 'sc_newshippingmethodtelemetry', 'sc_checkoutbannertelemetry', 'sc_learnmoreclcid', 'sc_satisfiedcheckout', 'sc_checkboxarialabel', 'sc_newlegaltextlayout', 'sc_newpagetitle', 'sc_prepaidcardsv3', 'sc_gamertaggifting', 'sc_checkoutargentinafee', 'sc_xboxcomasyncpurchase', 'sc_sameaddressdefault', 'sc_fixcolorcontrastforcheckout', 'sc_checkboxkg', 'sc_usebuynowbusinesslogic', 'sc_skippurchaseconfirm', 'sc_activitymonitorasyncpurchase', 'sc_shareddowngrade', 'sc_allowedpisenabled', 'sc_xboxoos', 'sc_eligibilityapi', 'sc_koreatransactionfeev1', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_cppidlerror', 'sc_bankchallenge', 'sc_allowelo', 'sc_delayretry', 'sc_loadtestheadersenabled', 'sc_migrationforcitizenspay', 'sc_conversionblockederror', 'sc_allowpaysafecard', 'sc_purchasedblocked', 'sc_outofstock', 'sc_selectpmonaddfailure', 'sc_allowcustompifiltering', 'sc_errorpageviewfix', 'sc_windowsdevkitname', 'sc_xboxredirection', 'sc_usebuynowonlynonprodendpoint', 'sc_getmoreinfourl', 'sc_disablefilterforuserconsent', 'sc_suppressrecoitem', 'sc_dcccattwo', 'sc_hipercard', 'sc_resellerdetail', 'sc_fixpidladdpisuccess', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_ineligibletostate', 'sc_greenshipping', 'sc_trackinitialcheckoutload', 'sc_creditcardpurge', 'sc_showlegalstringforproducttypepass', 'sc_newduplicatesubserror', 'sc_xboxgamepad', 'sc_xboxspinner', 'sc_xboxclosebutton', 'sc_xboxuiexp', 'sc_disabledefaultstyles', 'sc_gamertaggifting']
purchaseFlights = ['sc_appendconversiontype', 'sc_showvalidpis', 'sc_scdstextdirection', 'sc_optimizecheckoutload', 'sc_purchasedblockedby', 'sc_passthroughculture', 'sc_showcanceldisclaimerdefaultv1', 'sc_redirecttosignin', 'sc_paymentpickeritem', 'sc_cleanreducercode', 'sc_dimealipaystylingfix', 'sc_promocode', 'sc_onedrivedowngrade', 'sc_newooslogiconcart', 'sc_optionalcatalogclienttype', 'sc_klarna', 'sc_hidecontactcheckbox', 'sc_preparecheckoutrefactor', 'sc_checkoutklarna', 'sc_currencyformattingpkg', 'sc_fullpageredirectionforasyncpi', 'sc_xaaconversionerror', 'sc_promocodefeature-web-desktop', 'sc_eligibilityproducts', 'sc_disabledpaymentoption',
                   'sc_enablecartcreationerrorparsing', 'sc_purchaseblock', 'sc_returnoospsatocart', 'sc_dynamicseligibility', 'sc_usebuynowonlyinternalendpoint', 'sc_removemoreless', 'sc_renewalsubscriptionselector', 'sc_hidexdledd', 'sc_militaryshippingurl', 'sc_xboxdualleaf', 'sc_japanlegalterms', 'sc_multiplesubscriptions', 'sc_loweroriginalprice', 'sc_xaatovalenciastring', 'sc_cannotbuywarrantyalone', 'sc_showminimalfooteroncheckout', 'sc_checkoutdowngrade', 'sc_checkoutcontainsiaps', 'sc_localizedtax', 'sc_officescds', 'sc_disableupgradetrycheckout', 'sc_extendPageTagToOverride', 'sc_checkoutscenariotelemetry', 'sc_skipselectpi', 'sc_allowmpesapi', 'sc_purchasestatusmessage', 'sc_storetermslink', 'sc_postorderinfolineitemmessage', 'sc_addpaymentfingerprinttagging', 'sc_shippingallowlist', 'sc_emptyresultcheck', 'sc_dualleaf', 'sc_riskyxtoken', 'sc_abandonedretry', 'sc_testflightbuynow', 'sc_addshippingmethodtelemetry', 'sc_leaficons', 'sc_newspinneroverlay', 'sc_paymentinstrumenttypeandfamily', 'sc_addsitename', 'sc_disallowalipayforcheckout', 'sc_checkoutsignintelemetry', 'sc_prominenteddchange', 'sc_disableshippingaddressinit', 'sc_preparecheckoutperf',
                   'sc_buynowctatext', 'sc_buynowuiprod', 'sc_checkoutsalelegaltermsjp', 'sc_showooserrorforoneminute', 'sc_proratedrefunds', 'sc_entitlementcheckallitems', 'sc_indiaregsbanner', 'sc_checkoutentitlement', 'sc_rspv2', 'sc_focustrapforgiftthankyoupage', 'sc_hideneedhelp', 'sc_defaultshippingref', 'sc_uuid', 'sc_checkoutasyncpurchase', 'sc_nativeclientlinkredirect', 'sc_enablelegalrequirements', 'sc_expanded.purchasespinner', 'sc_valenciaupgrade', 'sc_enablezipplusfour', 'sc_giftingtelemetryfix', 'sc_handleentitlementerror', 'sc_alwayscartmuid', 'sc_sharedupgrade', 'sc_checkoutloadspinner', 'sc_xaaconversionexpirationdate', 'sc_helptypescript', 'sc_newdemandsandneedsstatement', 'sc_citizensoneallowed', 'sc_riskfatal', 'sc_renewtreatmenta', 'sc_trialtreatmenta', 'sc_cartzoomfix', 'sc_useofficeonlyinternalendpoint', 'sc_gotopurchase', 'sc_endallactivities', 'sc_headingheader', 'sc_flexsubs', 'sc_useanchorcomponent', 'sc_addbillingaddresstelemetry', 'sc_replacestoreappclient', 'sc_scenariotelemetryrefactor', 'sc_checkoutsmd', 'sc_scenariosupportupdate', 'sc_bankchallengecheckout', 'sc_addpaymenttelemetry', 'sc_railv2', 'sc_checkoutglobalpiadd', 'sc_reactcheckout', 'sc_xboxgotocart', 'sc_hidewarningevents', 'sc_xboxcomnosapi', 'sc_routebacktocartforoutofstock', 'sc_clientdebuginfo', 'sc_koreanlegalterms', 'sc_refactorprorate', 'sc_paymentoptionnotfound', 'sc_pidlflights', 'sc_fixcolorcontrastforrecommendeditems', 'sc_hideeditbuttonwhenediting', 'sc_enablekakaopay', 'sc_ordercheckoutfix', 'sc_xboxpmgrouping', 'sc_stickyfooter', 'sc_gotoredmrepl', 'sc_partnernametelemetry', 'sc_jpregionconversion', 'sc_checkoutorderedpv', 'sc_maxaddresslinelength', 'sc_componentexception', 'sc_buynowuipreload', 'sc_updatebillinginfo', 'sc_newshippingmethodtelemetry', 'sc_checkoutbannertelemetry', 'sc_learnmoreclcid', 'sc_satisfiedcheckout', 'sc_checkboxarialabel', 'sc_newlegaltextlayout', 'sc_newpagetitle', 'sc_prepaidcardsv3', 'sc_gamertaggifting', 'sc_checkoutargentinafee', 'sc_xboxcomasyncpurchase', 'sc_sameaddressdefault', 'sc_fixcolorcontrastforcheckout', 'sc_checkboxkg', 'sc_usebuynowbusinesslogic', 'sc_skippurchaseconfirm', 'sc_activitymonitorasyncpurchase', 'sc_shareddowngrade', 'sc_allowedpisenabled', 'sc_xboxoos', 'sc_eligibilityapi', 'sc_koreatransactionfeev1', 'sc_removesetpaymentmethod', 'sc_ordereditforincompletedata', 'sc_cppidlerror', 'sc_bankchallenge', 'sc_allowelo', 'sc_delayretry', 'sc_loadtestheadersenabled', 'sc_migrationforcitizenspay', 'sc_conversionblockederror', 'sc_allowpaysafecard', 'sc_purchasedblocked', 'sc_outofstock', 'sc_selectpmonaddfailure', 'sc_allowcustompifiltering', 'sc_errorpageviewfix', 'sc_windowsdevkitname', 'sc_xboxredirection', 'sc_usebuynowonlynonprodendpoint', 'sc_getmoreinfourl', 'sc_disablefilterforuserconsent', 'sc_suppressrecoitem', 'sc_dcccattwo', 'sc_hipercard', 'sc_resellerdetail', 'sc_fixpidladdpisuccess', 'sc_xdlshipbuffer', 'sc_allowverve', 'sc_inlinetempfix', 'sc_ineligibletostate', 'sc_greenshipping', 'sc_trackinitialcheckoutload', 'sc_creditcardpurge', 'sc_showlegalstringforproducttypepass', 'sc_newduplicatesubserror', 'sc_xboxgamepad', 'sc_xboxspinner', 'sc_xboxclosebutton', 'sc_xboxuiexp', 'sc_disabledefaultstyles', 'sc_gamertaggifting']


class GamepassPurchaser:

    def __init__(self, email: str, password: str, bin: str, ua: str):
        self.session = requests.Session()
        self.email = email
        self.password = password
        self.tools = tools()

        if "|" in bin:
            splited_bin = bin.split("|")

        if "," in bin:
            splited_bin = bin.split(",")

        if " " in bin:
            splited_bin = bin.split(" ")

        main_bin = splited_bin[0].replace("x", "")

        self.card_number = self.tools.generate_card(main_bin)
        self.expire_month = splited_bin[1] if splited_bin[1] != "rnd" else str(random.randint(01, 12))
        self.expire_year = splited_bin[2] if splited_bin[2] != "rnd" else str(
            random.randint(23, 29))
        self.cvv = splited_bin[3] if splited_bin[3] != "rnd" else str(
            random.randint(000, 999))

        if self.card_number[0] == "4":
            self.card_type = "visa"

        elif self.card_number[0] == "5":
            self.card_type = "mc"

        elif self.card_number[0] == "6":
            self.card_type = "amex"

        else:
            raise UnsupportedCard

        self.ua = ua
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'identity',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Sec-GPC': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': ua
        }

    def login_account(self):
        session = self.session
        response = session.get(
            'https://login.live.com/ppsecure/post.srf', headers=self.headers, timeout=20).text
        try:
            ppft = response.split(''''<input type="hidden" name="PPFT" id="i0327" value="''')[
                1].split('"')[0]
            login_url = response.split(",urlPost:'")[1].split("'")[0]
        except:
            raise ValueError

        login_data = f'i13=0&login={self.email}&loginfmt={self.email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={self.password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={ppft}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i19=449894'

        response = session.post(login_url, timeout=20 ,data=login_data, headers=self.headers).text
        try:
            ppft = re.findall("sFT:'(.+?(?=\'))", response)[0],
            login_url = re.findall("urlPost:'(.+?(?=\'))", response)[0]
            return ppft, login_url
        except:
            raise ValueError
