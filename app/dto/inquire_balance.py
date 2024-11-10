from dataclasses import dataclass
from typing import List

from pydantic.dataclasses import dataclass as pdataclass


@dataclass
class InquireBalanceRequestQuery:
    CANO: str
    """종합계좌번호"""
    ACNT_PRDT_CD: str
    """계좌상품코드"""
    AFHR_FLPR_YN: str
    """시간외단일가여부"""
    OFL_YN: str
    """오프라인여부"""
    INQR_DVSN: str
    """조회구분"""
    UNPR_DVSN: str
    """단가구분"""
    FUND_STTL_ICLD_YN: str
    """펀드결제분포함여부"""
    FNCG_AMT_AUTO_RDPT_YN: str
    """융자금액자동상환여부"""
    PRCS_DVSN: str
    """처리구분"""
    CTX_AREA_FK100: str
    """연속조회검색조건100"""
    CTX_AREA_NK100: str
    """연속조회키100"""


@pdataclass
class InquireBalanceResponse1:
    pdno: str
    """상품번호"""
    prdt_name: str
    """상품명"""
    trad_dvsn_name: str
    """매매구분명"""
    bfdy_buy_qty: str
    """전일매수수량"""
    bfdy_sll_qty: str
    """전일매도수량"""
    thdt_buyqty: str
    """금일매수수량"""
    thdt_sll_qty: str
    """금일매도수량"""
    hldg_qty: str
    """보유수량"""
    ord_psbl_qty: str
    """주문가능수량"""
    pchs_avg_pric: str
    """매입평균가격"""
    pchs_amt: str
    """매입금액"""
    prpr: str
    """현재가"""
    evlu_amt: str
    """평가금액"""
    evlu_pfls_amt: str
    """평가손익금액"""
    evlu_pfls_rt: str
    """평가손익율"""
    evlu_erng_rt: str
    """평가수익율"""
    loan_dt: str
    """대출일자"""
    loan_amt: str
    """대출금액"""
    stln_slng_chgs: str
    """대주매각대금"""
    expd_dt: str
    """만기일자"""
    fltt_rt: str
    """등락율"""
    bfdy_cprs_icdc: str
    """전일대비증감"""
    item_mgna_rt_name: str
    """종목증거금율명"""
    grta_rt_name: str
    """보증금율명"""
    sbst_pric: str
    """대용가격"""
    stck_loan_unpr: str
    """주식대출단가"""


@pdataclass
class InquireBalanceResponse2:
    dnca_tot_amt: str
    """예수금총금액"""
    nxdy_excc_amt: str
    """익일정산금액"""
    prvs_rcdl_excc_amt: str
    """가수도정산금액"""
    cma_evlu_amt: str
    """CMA평가금액"""
    bfdy_buy_amt: str
    """전일매수금액"""
    thdt_buy_amt: str
    """금일매수금액"""
    nxdy_auto_rdpt_amt: str
    """익일자동상환금액"""
    bfdy_sll_amt: str
    """전일매도금액"""
    thdt_sll_amt: str
    """금일매도금액"""
    d2_auto_rdpt_amt: str
    """D+2자동상환금액"""
    bfdy_tlex_amt: str
    """전일제비용금액"""
    thdt_tlex_amt: str
    """금일제비용금액"""
    tot_loan_amt: str
    """총대출금액"""
    scts_evlu_amt: str
    """유가평가금액"""
    tot_evlu_amt: str
    """총평가금액"""
    nass_amt: str
    """순자산금액"""
    fncg_gld_auto_rdpt_yn: str
    """융자금자동상환여부"""
    pchs_amt_smtl_amt: str
    """매입금액합계금액"""
    evlu_amt_smtl_amt: str
    """평가금액합계금액"""
    evlu_pfls_smtl_amt: str
    """평가손익합계금액"""
    tot_stln_slng_chgs: str
    """총대주매각대금"""
    bfdy_tot_asst_evlu_amt: str
    """전일총자산평가금액"""
    asst_icdc_amt: str
    """자산증감액"""
    asst_icdc_erng_rt: str
    """자산증감수익율"""


@pdataclass
class InquireBalanceResponse:
    rt_cd: str
    msg_cd: str
    msg1: str
    ctx_area_fk100: str
    ctx_area_nk100: str
    output1: List[InquireBalanceResponse1]
    output2: List[InquireBalanceResponse2]