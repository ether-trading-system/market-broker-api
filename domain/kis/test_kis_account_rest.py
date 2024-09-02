import pytest

from .kis_account_rest import KisAccountRest


@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_balance():
    async with KisAccountRest() as rest:
        res = await rest.get_balance(
            app_key='',
            app_secret=''
        )

        # {
        #   "ctx_area_fk100": "63792537^01^N^N^00^01^Y^                                                                            ",
        #   "ctx_area_nk100": "                                                                                                    ",
        #   "output1": [],
        #   "output2": [
        #     {
        #       "dnca_tot_amt": "0",
        #       "nxdy_excc_amt": "0",
        #       "prvs_rcdl_excc_amt": "0",
        #       "cma_evlu_amt": "0",
        #       "bfdy_buy_amt": "0",
        #       "thdt_buy_amt": "0",
        #       "nxdy_auto_rdpt_amt": "0",
        #       "bfdy_sll_amt": "0",
        #       "thdt_sll_amt": "0",
        #       "d2_auto_rdpt_amt": "0",
        #       "bfdy_tlex_amt": "0",
        #       "thdt_tlex_amt": "0",
        #       "tot_loan_amt": "0",
        #       "scts_evlu_amt": "0",
        #       "tot_evlu_amt": "0",
        #       "nass_amt": "0",
        #       "fncg_gld_auto_rdpt_yn": "",
        #       "pchs_amt_smtl_amt": "0",
        #       "evlu_amt_smtl_amt": "0",
        #       "evlu_pfls_smtl_amt": "0",
        #       "tot_stln_slng_chgs": "0",
        #       "bfdy_tot_asst_evlu_amt": "0",
        #       "asst_icdc_amt": "0",
        #       "asst_icdc_erng_rt": "0.00000000"
        #     }
        #   ],
        #   "rt_cd": "0",
        #   "msg_cd": "KIOK0560",
        #   "msg1": "조회할 내용이 없습니다                                                          "
        # }

        print(res)
