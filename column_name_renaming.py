#!/usr/bin/env python
# encoding: utf-8


col_shortener = {
    'Q1':'confirm',
    'Q2':'faculty',
    'Q3':'funder',
    'Q4':'position',
    'Q5':'rs_use',
    'Q6':'rs_importance',
    'Q7':'rs_devel',
    'Q8':'rs_devel_expertise',
    'Q9':'rs_training',
    'Q10':'rs_commercialise',
    'Q11':'rs_release',
    'Q12':'hpc_use',
    'Q13_1':'version_control',
    'Q13_2':'unit_reg_test',
    'Q13_3':'continuous_integration',
    'Q13_4':'compilation',
    'Q13_5':'documentation',
    'Q14':'uni_support',
    'Q15':'hired',
    'Q16':'costed',
    'Q17_1':'full_time_devel',
    'Q17_2':'pool_devel',
    'Q18':'voucher',
    'Q19':'consulting',
    'Q20':'mailing'
}


add_an_other_category = [
    'funders',
    'job_title',
    'hpc_use'
]


sort_no_further_analysis = [
    'faculty',
    'funders',
    'job_title',
    'hpc_use'
]

yes_no_analysis = [
    'use_software',
    'develop_own_code',
    'training',
    'want_to_commercialise',
    'ready_to_share',
    'hired_developer'
]

scale_analysis = [
    'importance_software',
    'development_expertise',
    'current_support'
]

worded_scale_analysis = [
    'version_control',
    'continuous_integration',
    'unit_testing',
    'funds_for_development',
    'hire_full_time_developer',
    'hire_rse'
]
