#!/usr/bin/env python
# encoding: utf-8


col_shortener = {
    'Q1':'confirm',
    'Q2':'faculty',
    'Q3':'department',
    'Q4':'funders',
    'Q5':'position',
    'Q6':'use_software',
    'Q7':'importance_software',
    'Q8':'develop_own_code',
    'Q9':'development_expertise',
    'Q10':'sufficient_training',
    'Q11':'want_to_commercialise',
    'Q12':'ready_to_release',
    'Q13':'hpc_use',
    'Q14_1':'version_control',
    'Q14_2':'unit_regression_testing',
    'Q14_3':'continuous_integration',
    'Q14_4':'compilation',
    'Q14_5':'documentation',
    'Q15':'uni_support',
    'Q16':'hired_developer',
    'Q17':'costed_developer',
    'Q18_1':'hire_full_time_developer',
    'Q18_2':'hire_pool_developer',
    'Q19':'voucher',
    'Q20':'consulting',
    'Q21':'mailing'
}


add_an_other_category = [
    'funders',
    'position',
    'hpc_use'
]


sort_no_further_analysis = [
    'faculty',
    'funders',
    'position',
    'hpc_use'
]

yes_no_analysis = [
    'use_software',
    'develop_own_code',
    'sufficient_training',
    'want_to_commercialise',
    'ready_to_release',
    'hired_developer'
]

scale_analysis = [
    'importance_software',
    'development_expertise',
    'sufficient_training'
]

worded_scale_analysis = [
    'version_control',
    'continuous_integration',
    'unit_regression_testing',
    'hire_full_time_developer',
    'hire_pool_developer'
]
