# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = cdm_cohort_from_dict(json.loads(json_string))

"""
This file generated using: https://app.quicktype.io/
ATLAS stores cohort definitions details in ohdsi.cohort_definition_details
The structure is: id, expression, hash_code
This class represents the 'expression' field.

The ohdsi.cohort_definition has id, name and created_date

"""
from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class CensorWindow:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'CensorWindow':
        assert isinstance(obj, dict)
        return CensorWindow()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class CollapseSettings:
    collapse_type: str
    era_pad: int

    @staticmethod
    def from_dict(obj: Any) -> 'CollapseSettings':
        assert isinstance(obj, dict)
        collapse_type = from_str(obj.get("CollapseType"))
        era_pad = from_int(obj.get("EraPad"))
        return CollapseSettings(collapse_type, era_pad)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CollapseType"] = from_str(self.collapse_type)
        result["EraPad"] = from_int(self.era_pad)
        return result


@dataclass
class Concept:
    concept_id: int
    concept_name: str
    standard_concept: str
    standard_concept_caption: str
    invalid_reason: str
    invalid_reason_caption: str
    concept_code: int
    domain_id: str
    vocabulary_id: str
    concept_class_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Concept':
        assert isinstance(obj, dict)
        concept_id = from_int(obj.get("CONCEPT_ID"))
        concept_name = from_str(obj.get("CONCEPT_NAME"))
        standard_concept = from_str(obj.get("STANDARD_CONCEPT"))
        standard_concept_caption = from_str(obj.get("STANDARD_CONCEPT_CAPTION"))
        invalid_reason = from_str(obj.get("INVALID_REASON"))
        invalid_reason_caption = from_str(obj.get("INVALID_REASON_CAPTION"))
        concept_code = int(from_str(obj.get("CONCEPT_CODE")))
        domain_id = from_str(obj.get("DOMAIN_ID"))
        vocabulary_id = from_str(obj.get("VOCABULARY_ID"))
        concept_class_id = from_str(obj.get("CONCEPT_CLASS_ID"))
        return Concept(concept_id, concept_name, standard_concept, standard_concept_caption, invalid_reason,
                       invalid_reason_caption, concept_code, domain_id, vocabulary_id, concept_class_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CONCEPT_ID"] = from_int(self.concept_id)
        result["CONCEPT_NAME"] = from_str(self.concept_name)
        result["STANDARD_CONCEPT"] = from_str(self.standard_concept)
        result["STANDARD_CONCEPT_CAPTION"] = from_str(self.standard_concept_caption)
        result["INVALID_REASON"] = from_str(self.invalid_reason)
        result["INVALID_REASON_CAPTION"] = from_str(self.invalid_reason_caption)
        result["CONCEPT_CODE"] = from_str(str(self.concept_code))
        result["DOMAIN_ID"] = from_str(self.domain_id)
        result["VOCABULARY_ID"] = from_str(self.vocabulary_id)
        result["CONCEPT_CLASS_ID"] = from_str(self.concept_class_id)
        return result


@dataclass
class Item:
    concept: Concept
    is_excluded: bool
    include_descendants: bool
    include_mapped: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        concept = Concept.from_dict(obj.get("concept"))
        is_excluded = from_bool(obj.get("isExcluded"))
        include_descendants = from_bool(obj.get("includeDescendants"))
        include_mapped = from_bool(obj.get("includeMapped"))
        return Item(concept, is_excluded, include_descendants, include_mapped)

    def to_dict(self) -> dict:
        result: dict = {}
        result["concept"] = to_class(Concept, self.concept)
        result["isExcluded"] = from_bool(self.is_excluded)
        result["includeDescendants"] = from_bool(self.include_descendants)
        result["includeMapped"] = from_bool(self.include_mapped)
        return result


@dataclass
class Expression:
    items: List[Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Expression':
        assert isinstance(obj, dict)
        items = from_list(Item.from_dict, obj.get("items"))
        return Expression(items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        return result


@dataclass
class ConceptSet:
    id: int
    name: str
    expression: Expression

    @staticmethod
    def from_dict(obj: Any) -> 'ConceptSet':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        expression = Expression.from_dict(obj.get("expression"))
        return ConceptSet(id, name, expression)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["expression"] = to_class(Expression, self.expression)
        return result


@dataclass
class Limit:
    type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Limit':
        assert isinstance(obj, dict)
        type = from_str(obj.get("Type"))
        return Limit(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Type"] = from_str(self.type)
        return result


@dataclass
class Observation:
    codeset_id: int
    observation_type_exclude: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Observation':
        assert isinstance(obj, dict)
        codeset_id = from_int(obj.get("CodesetId"))
        observation_type_exclude = from_bool(obj.get("ObservationTypeExclude"))
        return Observation(codeset_id, observation_type_exclude)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CodesetId"] = from_int(self.codeset_id)
        result["ObservationTypeExclude"] = from_bool(self.observation_type_exclude)
        return result


@dataclass
class CriteriaList:
    observation: Observation

    @staticmethod
    def from_dict(obj: Any) -> 'CriteriaList':
        assert isinstance(obj, dict)
        observation = Observation.from_dict(obj.get("Observation"))
        return CriteriaList(observation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Observation"] = to_class(Observation, self.observation)
        return result


@dataclass
class ObservationWindow:
    prior_days: int
    post_days: int

    @staticmethod
    def from_dict(obj: Any) -> 'ObservationWindow':
        assert isinstance(obj, dict)
        prior_days = from_int(obj.get("PriorDays"))
        post_days = from_int(obj.get("PostDays"))
        return ObservationWindow(prior_days, post_days)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PriorDays"] = from_int(self.prior_days)
        result["PostDays"] = from_int(self.post_days)
        return result


@dataclass
class PrimaryCriteria:
    criteria_list: List[CriteriaList]
    observation_window: ObservationWindow
    primary_criteria_limit: Limit

    @staticmethod
    def from_dict(obj: Any) -> 'PrimaryCriteria':
        assert isinstance(obj, dict)
        criteria_list = from_list(CriteriaList.from_dict, obj.get("CriteriaList"))
        observation_window = ObservationWindow.from_dict(obj.get("ObservationWindow"))
        primary_criteria_limit = Limit.from_dict(obj.get("PrimaryCriteriaLimit"))
        return PrimaryCriteria(criteria_list, observation_window, primary_criteria_limit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CriteriaList"] = from_list(lambda x: to_class(CriteriaList, x), self.criteria_list)
        result["ObservationWindow"] = to_class(ObservationWindow, self.observation_window)
        result["PrimaryCriteriaLimit"] = to_class(Limit, self.primary_criteria_limit)
        return result


@dataclass
class CdmCohort:
    cdm_version_range: str
    primary_criteria: PrimaryCriteria
    concept_sets: List[ConceptSet]
    qualified_limit: Limit
    expression_limit: Limit
    inclusion_rules: List[Any]
    censoring_criteria: List[Any]
    collapse_settings: CollapseSettings
    censor_window: CensorWindow

    @staticmethod
    def from_dict(obj: Any) -> 'CdmCohort':
        assert isinstance(obj, dict)
        cdm_version_range = from_str(obj.get("cdmVersionRange"))
        primary_criteria = PrimaryCriteria.from_dict(obj.get("PrimaryCriteria"))
        concept_sets = from_list(ConceptSet.from_dict, obj.get("ConceptSets"))
        qualified_limit = Limit.from_dict(obj.get("QualifiedLimit"))
        expression_limit = Limit.from_dict(obj.get("ExpressionLimit"))
        inclusion_rules = from_list(lambda x: x, obj.get("InclusionRules"))
        censoring_criteria = from_list(lambda x: x, obj.get("CensoringCriteria"))
        collapse_settings = CollapseSettings.from_dict(obj.get("CollapseSettings"))
        censor_window = CensorWindow.from_dict(obj.get("CensorWindow"))
        return CdmCohort(cdm_version_range, primary_criteria, concept_sets, qualified_limit, expression_limit,
                         inclusion_rules, censoring_criteria, collapse_settings, censor_window)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cdmVersionRange"] = from_str(self.cdm_version_range)
        result["PrimaryCriteria"] = to_class(PrimaryCriteria, self.primary_criteria)
        result["ConceptSets"] = from_list(lambda x: to_class(ConceptSet, x), self.concept_sets)
        result["QualifiedLimit"] = to_class(Limit, self.qualified_limit)
        result["ExpressionLimit"] = to_class(Limit, self.expression_limit)
        result["InclusionRules"] = from_list(lambda x: x, self.inclusion_rules)
        result["CensoringCriteria"] = from_list(lambda x: x, self.censoring_criteria)
        result["CollapseSettings"] = to_class(CollapseSettings, self.collapse_settings)
        result["CensorWindow"] = to_class(CensorWindow, self.censor_window)
        return result


def cdm_cohort_from_dict(s: Any) -> CdmCohort:
    return CdmCohort.from_dict(s)


def cdm_cohort_to_dict(x: CdmCohort) -> Any:
    return to_class(CdmCohort, x)
