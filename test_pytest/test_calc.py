from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

import pytest
import yaml

from test_pytest.Calculator import Calculator


def get_data(level):
    with open("./data/data.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        # print(type(datas),datas)
        return (datas.get("add").get(level).get("datas"), datas.get("add").get(level).get("ids"))


def change_to_decimal(num):
    # 四舍五入的运算模式
    return Decimal(f"{num}").quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)


class TestCalc:
    P0_data, P0_ids = get_data("P0")
    P11_data, P11_ids = get_data("P1_1")
    P12_data, P12_ids = get_data("P1_2")
    P13_data, P13_ids = get_data("P1_3")
    P2_data, P2_ids = get_data("P2")

    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_calss(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect', P0_data, ids=P0_ids)
    def test_add_caseP0(self, a, b, expect):
        assert change_to_decimal(expect) == self.calc.add(change_to_decimal(a), change_to_decimal(b))

    @pytest.mark.parametrize('a,b,expect', P11_data, ids=P11_ids)
    def test_add_caseP11(self, a, b, expect):
        assert change_to_decimal(expect) == self.calc.add(change_to_decimal(a), change_to_decimal(b))

    @pytest.mark.parametrize('a,b,expect', P12_data, ids=P12_ids)
    def test_add_caseP12(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', P13_data, ids=P13_ids)
    def test_add_caseP13(self, a, b, expect):
        # case不建议使用try except
        # try:
        #     assert expect == self.calc.add(a, b)
        # except TypeError:
        #     print("类型错误")
        with pytest.raises(TypeError) as e:
            result = self.calc.add(a, b)
        assert expect == e.typename

    @pytest.mark.parametrize('a,b,expect', P2_data, ids=P2_ids)
    def test_add_caseP2(self, a, b, expect):
        with pytest.raises(TypeError) as e:
            result = self.calc.add(a, b)
        assert expect == e.typename
