# -*- coding: utf-8 -*-
"""
Created on Wed May 17 

@author: AM Datalyst
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def recodeValues(coded, columnName, df, string = True):
        if string == True:
            filtered = df[columnName].astype('str')
        else:
            filtered = df[columnName]
            
        filtered = pd.DataFrame(filtered)
        
        filtered = filtered.replace({columnName: coded})
        
        return filtered

def cleanData(fileLocation, fileName):
    # Reading the dataset
    data = pd.read_excel(fileLocation + '/' + fileName)
    
    
    # =============================================================================
    # # for DM1 - company
    # =============================================================================
    
    DM1 = data[['DM1', 'DM1r6oe']]
    
    merged_column = DM1.apply(lambda row: 'Others - ' + row['DM1r6oe'] if row['DM1'] == 6 else row['DM1'], axis=1)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'Financial Services Industry', 2.0:'Games Industry', 3.0:'Film / VFX Industry', 
                   4.0:'Advertising or Marketing Industry', 5.0:'Fashion Industry'}
    
    DM1_company = DM1Merged.replace({0:codedValues})
    
    # =============================================================================
    # # for DM2 - company_types
    # =============================================================================
    codedValues = {'1':'Content', '2':'Hardware', '3':'Distribution', '4':'Retailer', '5':'None of the above'}
    
    DM2_companyTypes = recodeValues(codedValues, 'DM2', data)
    
    # =============================================================================
    # # for DM3 - game_produced
    # =============================================================================
    codedValues = {'1':'0', '2':'1-2', '3':'3-5', '4':'6-10', '5':'More than 10'}
    
    DM3_gameProduced = recodeValues(codedValues, 'DM3', data)
    
    
    # =============================================================================
    # # for DM4a - studio_type
    # =============================================================================
    codedValues = {'1':'Hobbyist', '2':'Freelancer', '3':'Indie (1-9)', '4':'Small (10-49)', 
                   '5':'Medium (50-99)', '6':'Large (100+)'}
    
    DM4_studioType = recodeValues(codedValues, 'DM4_a', data)
    
    # =============================================================================
    # # for DM4 - studioOwnType
    # =============================================================================
    # Define the text corresponding to each index for DM4
    columnDict = {0: 'Publisher-owned', 1: 'Outsource service provider', 2: 'Venture-backed'}
    
    DM4 = data[['DM4_br7', 'DM4_br8', 'DM4_br9']]
    DM4_ownType = pd.DataFrame()
    
    for i, row in DM4.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['studioOwnType'] = titles
        DM4_ownType = DM4_ownType.append(row)
    
    DM4_ownType['studioOwnType'] = DM4_ownType['studioOwnType'].apply(lambda x: x if isinstance(x, list) else [])
    DM4_ownType = DM4_ownType['studioOwnType']
    
    # =============================================================================
    # # for DM5 - titles
    # =============================================================================
    # Define the text corresponding to each index for DM5
    columnDict = {0: 'Hypercasual', 1: 'Casual', 2: 'Midcore', 3: 'AA', 4: 'AAA', 
                  5: 'All of the above', 6: 'None of the above'}
    
    DM5 = data[['DM5r1', 'DM5r2', 'DM5r3', 'DM5r4', 'DM5r5', 'DM5r6', 'DM5r7']]
    DM5_titles = pd.DataFrame()
    
    for i, row in DM5.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['titles'] = titles
        DM5_titles = DM5_titles.append(row)
    
    DM5_titles['titles'] = DM5_titles['titles'].apply(lambda x: x if isinstance(x, list) else [])
    DM5_titles = DM5_titles['titles']
    
    # =============================================================================
    # # for DM6 - platforms
    # =============================================================================
    # Define the text corresponding to each index for DM6
    columnDict = {0: 'Web', 1: 'Mobile', 2: 'PC', 3: 'Console (Xbox, Playstation, Switch)', 
                  4: 'AR/VR', 5: 'All of the above', 6: 'None of the above'}
    
    DM6 = data[['DM6r1', 'DM6r2', 'DM6r3', 'DM6r4', 'DM6r5', 'DM6r6', 'DM6r7']]
    DM6_platforms = pd.DataFrame()
    
    for i, row in DM6.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['platforms'] = titles
        DM6_platforms = DM6_platforms.append(row)
    
    DM6_platforms['platforms'] = DM6_platforms['platforms'].apply(lambda x: x if isinstance(x, list) else [])
    DM6_platforms = DM6_platforms['platforms']
    
    
    # =============================================================================
    # # for DM7 - currentRole
    # =============================================================================
    
    DM7 = data[['DM7', 'DM7r10oe']]
    
    merged_column = DM7.apply(lambda row: 'Others - ' + row['DM7r10oe'] if row['DM7'] == 10 else row['DM7'], axis=1)
    
    DM7Merged = pd.DataFrame(merged_column)
    
    
    codedValues = {1.0:'Studio Management', 2.0:'Production', 3.0:'Artist & content creation', 
                   4.0:'Developer & software engineer', 5.0:'QA & testing', 6.0:'Data, analytics, monetization', 
                   7.0:'Finance', 8.0:'Legal & HR', 9.0:'Events'}
    
    DM7_currentRole = DM7Merged.replace({0:codedValues})
    
    # =============================================================================
    # # for PL7 - production_role
    # =============================================================================
    codedValues = {'1.0':'Production leading up to a title release',
                   '2.0':'Live services production after a title has been released', 
                   '3.0':'Both pre and post release production',
                   '4.0':'Not Applicable'}
    
    PL7_productionRole = recodeValues(codedValues, 'PL7', data)
    
    # =============================================================================
    # # for DM8 - other_industry_work
    # =============================================================================
    codedValues = {'1':'Yes',
                   '2':'Yes, but not significant ', 
                   '3':'No'}
    
    DM8_otherIndustryWork = recodeValues(codedValues, 'DM8', data)
    
    
    # =============================================================================
    # # for DM9 - work_Location_Frequency
    # =============================================================================
    
    
    DM9 = data[['DM9', 'DM9r8oe']]
    
    merged_column = DM9.apply(lambda row: 'Others - ' + row['DM9r8oe'] if row['DM9'] == 8 else row['DM9'], axis=1)
    
    DM9Merged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'US', 2.0:'Canada', 3.0:'EU', 4.0:'UK', 5.0:'Japan', 6.0:'Korea', 7.0:'China'}
    
    DM9_location_frequency = DM9Merged.replace({0:codedValues})
    
    
    # =============================================================================
    # # for DM9A - your_work_types
    # =============================================================================
    codedValues = {'1':'I work in an office every day',
                   '2':'I split my time between remote and in-office', 
                   '3':'I always work from home/remotely'}
    
    DM9a_yourWorkTypes = recodeValues(codedValues, 'DM9a', data)
    
    
    
    # =============================================================================
    # # for IT1A ORDER - industry-trends-challenges(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for IT1A
    columnDict = {'1':'cost_rising', 
                  '2':'from_hypercasual_to_midcore',
                  '3':'player_demand_AA/AAA_game_quality', 
                  '4':'cross_platform_multiplayer-studio_support_needed',
                  '5':'use_data_analytics',
                  '6':'live_services_needed', 
                  '7':'scarcity_challenges_studio_growth',
                  '' :''}
    
    
    IT1A = data[['IT1A_Orderr1', 'IT1A_Orderr2', 'IT1A_Orderr3', 'IT1A_Orderr4',
                 'IT1A_Orderr5', 'IT1A_Orderr6', 'IT1A_Orderr7']]
    
    IT1A_orders = pd.DataFrame()
    
    for i, row in IT1A.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        IT1A_orders = IT1A_orders.append([result_list])
      
    IT1A_orders = IT1A_orders.reset_index(drop = True)    
    IT1A_orders['order'] = IT1A_orders.values.tolist()
    IT1A_orders = IT1A_orders['order']
    
    
    # =============================================================================
    # # for IT2 - game_engine
    # =============================================================================
    codedValues = {'1':'Unity',
                   '2':'Unreal Engine', 
                   '3':'Godot',
                   '4':'Proprietary Engine',
                   '5':'No - open-source framework'}
    
    IT2_gameEngine = recodeValues(codedValues, 'IT2', data)
    
    
    # =============================================================================
    # # for IT2A - other_game_engine
    # =============================================================================
    
    IT2A = data[['IT2A', 'IT2Ar5oe']]
    
    merged_column = IT2A.apply(lambda row: 'Others - ' + row['IT2Ar5oe'] if row['IT2A'] == 5 else row['IT2A'], axis=1)
    
    IT2AMerged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'Yes, Unity', 2.0:'Yes, Unreal Engine', 3.0:'Yes, Godot', 
                   4.0:'Yes, Proprietary Engine', 6.0:'No'}
    
    IT2A_other_game_engine = IT2AMerged.replace({0: codedValues})
    
    
    # =============================================================================
    # # for IT3 - live_services_title
    # =============================================================================
    codedValues = {'1':'Currently working on a title with live services',
                   '2':'Intend to release or transition a title to a live services model', 
                   '3':'No plans for live services in any upcoming title'}
    
    IT3_liveServicesTitle = recodeValues(codedValues, 'IT3', data)
    
    
    # =============================================================================
    # # for IT4 - cloudTechnologyUsage
    # =============================================================================
    codedValues = {'1':'Yes, in production',
                   '2':'Yes, experimenting', 
                   '3':'No, but interested',
                   '4':'No, and not interested'}
    
    IT4_cloudTechnologyUsage = recodeValues(codedValues, 'IT4', data)
    
    
    
    # =============================================================================
    # # for IT4A ORDER - migrating_to_cloud_concerns(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for IT4A
    columnDict = {'1':'performance_concerns',
                 '2':'cost_cocenrs',
                 '3':'reliability_concerns',
                 '4':'data_privacy_concenrs',
                 '5':'learning_curve_concerns',
                 '6':'no_internal_expertise',
                 '7':'no_product_meet_needs',
                 '8':'no_concerns',
                  '' :''}
    
    
    IT4A = data[['IT4a_Orderr1', 'IT4a_Orderr2', 'IT4a_Orderr3', 'IT4a_Orderr4', 'IT4a_Orderr5',
                 'IT4a_Orderr6', 'IT4a_Orderr7', 'IT4a_Orderr8']]
                 
    IT4A_orders = pd.DataFrame()
    
    for i, row in IT4A.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        IT4A_orders = IT4A_orders.append([result_list])
      
    IT4A_orders = IT4A_orders.reset_index(drop = True)    
    IT4A_orders['order'] = IT4A_orders.values.tolist()
    IT4A_orders = IT4A_orders['order']
    
    # =============================================================================
    # # for IT5 - studio_title
    # =============================================================================
    codedValues = {'1':'Currently working on a title built on blockchain technology',
                   '2':'Intend to support or transition to a blockchain infrastructure', 
                   '3':'No plans to incorporate blockchain technology in a future title'}
    
    IT5_studioTitle = recodeValues(codedValues, 'IT5', data)
    
    # =============================================================================
    # # for IT6r9 - impact_by_AI_on_development
    # =============================================================================
    
    
    IT6r9 = data[['IT6r9', 'IT6r9oe']]
    
    merged_column = IT6r9.apply(lambda row: 'Others - ' + row['IT6r9oe'] if row['IT6r9'] == 5 else row['IT6r9'], axis=1)
    
    
    IT6r9Merged = pd.DataFrame(merged_column)
    
    codedValues = {0.0:'No', 1.0:'Yes'}
    
    IT6r9 = IT6r9Merged.replace({0:codedValues})
    
    
    
    # =============================================================================
    # # for IT6 ORDER - impact_by_AI_on_development (most to least)
    # =============================================================================
    
    # Define the text corresponding to each index for IT6
    columnDict = {'1':'artist_content_creation',
                 '2':'game_engine_programming',
                 '3':'testing_and_QA_processes',
                 '4':'narrative_&_story',
                 '5':'game_design',
                 '6':'intelligent_npcs',
                 '7':'player-generated_content',
                 '8':'audio/language_generation',
                  '' :''}
    
    
    IT6 = data[['IT6_Orderr1', 'IT6_Orderr2', 'IT6_Orderr3', 'IT6_Orderr4', 'IT6_Orderr5',
                 'IT6_Orderr6', 'IT6_Orderr7', 'IT6_Orderr8']]
                 
    IT6_orders = pd.DataFrame()
    
    for i, row in IT6.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        IT6_orders = IT6_orders.append([result_list])
      
    IT6_orders = IT6_orders.reset_index(drop = True)    
    IT6_orders['order'] = IT6_orders.values.tolist()
    IT6_orders = IT6_orders['order']
    
    # =============================================================================
    # # for IT6a - AI_replace_Employee
    # =============================================================================
    codedValues = {'1':'It already is',
                   '2':'1-2 years', 
                   '3':'3-5 years',
                   '4':'5+ years',
                   '5':'Never'}
    
    IT6a_AI_replace_Employee = recodeValues(codedValues, 'IT6a', data)
    
    
    # =============================================================================
    # # ART
    # =============================================================================
    
    # =============================================================================
    # # for A1 - artistType
    # =============================================================================
    A1 = data[['A1', 'A1r9oe']]
    
    merged_column = A1.apply(lambda row: 'Others - ' + row['A1r9oe'] if row['A1'] == 9.0 else row['A1'], axis=1)
    
    
    A1Merged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'Concept artist', 2.0:'Modeler', 3.0:'Texture artist', 4.0:'Character artist',
                   5.0:'Environment artist', 6.0:'VFX artist (e.g. particles, effects)', 
                   7.0:'UI designer', 8.0:'Technical artist'}
    
    A1Merged = A1Merged.replace({0:codedValues})
    
    
    # =============================================================================
    # # for A11 - cost_change_3D_content
    # =============================================================================
    codedValues = {1.0:'Becoming more expensive',
                   2.0:'Becoming less expensive', 
                   3.0:'Not changing'}
    
    A11_costChange3D = recodeValues(codedValues, 'A11', data, string = False)
    
    
    
    # =============================================================================
    # # for A11a ORDER - reason_for_increase(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for A11a
    columnDict = {'1': 'The required quality of game assets is rising', 
                  '2': 'Game environments are becoming larger',
                  '3': 'More realistic character animation',
                  '4': 'Talent is more costly', 
                  '5':'More complex game design',
                  '' :''}
    
    
    A11a = data[['A11ar1', 'A11ar2', 'A11ar3', 'A11ar4', 'A11ar5']]
                 
    A11a_orders = pd.DataFrame()
    
    for i, row in A11a.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        A11a_orders = A11a_orders.append([result_list])
      
    A11a_orders = A11a_orders.reset_index(drop = True)    
    A11a_orders['order'] = A11a_orders.values.tolist()
    A11a_orders = A11a_orders['order']
    
    
    
    # =============================================================================
    # # for A11b ORDER - reason_for_decrease(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for A11b
    columnDict = {'1': 'Better DCC tools', 
                  '2': 'Reusing assets',
                  '3': 'Using prefab assets',
                  '4': 'AI tools', 
                  '5':'More outsourcers available',
                  '' :''}
    
    A11b = data[['A11br1', 'A11br2', 'A11br3', 'A11br4', 'A11br5']]
                 
    A11b_orders = pd.DataFrame()
    
    for i, row in A11b.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        A11b_orders = A11b_orders.append([result_list])
      
    A11b_orders = A11b_orders.reset_index(drop = True)    
    A11b_orders['order'] = A11b_orders.values.tolist()
    A11b_orders = A11b_orders['order']
    
    
    # =============================================================================
    # # for A16 Others
    # =============================================================================
    A16r6 = data[['A16r6', 'A16r6oe']]
    
    merged_column = A16r6.apply(lambda row: 'Others - ' + row['A16r6oe'] if row['A16r6'] == 6 else row['A16r6'], axis=1)
    
    A16r6Merged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'Using in production', 
                   2.0:'Experimenting with', 
                   3.0:'Not using', 
                   4.0:'Not interested'}
    
    A16r6 = A16r6Merged.replace({0:codedValues})
    
    
    # =============================================================================
    # # Dev and Engineering
    # =============================================================================
    
    # =============================================================================
    # # for DE16 Others
    # =============================================================================
    DE16 = data[['DE16', 'DE16r4oe']]
    
    merged_column = DE16.apply(lambda row: 'Others - ' + row['DE16r4oe'] if row['DE16'] == 4.0 else row['DE16'], axis=1)
    
    DE16Merged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'Git', 
                   2.0:'Perforce', 
                   3.0:'Plastic', 
                   5.0:'None'}
    
    DE16_pipelineTool = DE16Merged.replace({0:codedValues})
    
    
    # =============================================================================
    # # for DE16a - building_pipeline_problems
    # =============================================================================
    # Define the text corresponding to each index for DE16ar
    columnDict = {0: 'Poor merging tools', 1: 'Performance', 2: 'Reliability',
                  3: 'Ease of use', 4:'Broken or partial submits', 5: 'Disk Space', 6:'None of these'}
    
    DE16a = data[['DE16ar1', 'DE16ar2', 'DE16ar3', 'DE16ar4', 'DE16ar5', 'DE16ar6', 'DE16ar7']]
    
    DE16a_pipelineProblems = pd.DataFrame()
    
    for i, row in DE16a.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['pipeline_problems'] = titles
        DE16a_pipelineProblems = DE16a_pipelineProblems.append(row)
    
    DE16a_pipelineProblems['pipeline_problems'] = DE16a_pipelineProblems['pipeline_problems'].apply(lambda x: x if isinstance(x, list) else [])
    DE16a_pipelineProblems = DE16a_pipelineProblems['pipeline_problems']
    
    
    # =============================================================================
    # # for DE17a - practices_implemented
    # =============================================================================
    # Define the text corresponding to each index for DE16ar
    columnDict = {0: 'Continuous integration', 1: 'Continuous delivery', 2: 'Automated smoke testing',
                  3: 'Automated unit testing', 4:'Staging & dev enviroments',
                  5: 'Monitoring & logging incident reports', 6:'None of these'}
    
    DE17a = data[['DE17ar1', 'DE17ar2', 'DE17ar3', 'DE17ar4', 'DE17ar5', 'DE17ar6', 'DE17ar7']]
    
    DE17a_practicesImplemented = pd.DataFrame()
    
    for i, row in DE17a.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['practices_implemented'] = titles
        DE17a_practicesImplemented = DE17a_practicesImplemented.append(row)
    
    DE17a_practicesImplemented['practices_implemented'] = DE17a_practicesImplemented['practices_implemented'].apply(
            lambda x: x if isinstance(x, list) else [])
    DE17a_practicesImplemented = DE17a_practicesImplemented['practices_implemented']
    
    
    # =============================================================================
    # # TESTING
    # =============================================================================
    
    # =============================================================================
    # # for T11d Others
    # =============================================================================
    T11d = data[['T11d', 'T11dr5oe']]
    
    merged_column = T11d.apply(lambda row: 'Others - ' + row['T11dr5oe'] if row['T11d'] == 5.0 else row['T11d'], axis=1)
    
    T11dMerged = pd.DataFrame(merged_column)
    
    codedValues = {1.0:'Not prioritized by leadership', 
                   2.0:'Not enough budget for headcount', 
                   3.0:'Production timeline could not support more time', 
                   4.0:'Unable to test quickly or effectively'}
    
    T11d_whyNot = T11dMerged.replace({0:codedValues})
    
    
    
    # =============================================================================
    # # for T12 - testings_conducted
    # =============================================================================
    # Define the text corresponding to each index for T12
    columnDict = {0: 'Smoke tests', 1: 'Unit tests', 2: 'Asset validation',
                  3: 'Performance tests', 4:'Regression tests', 5: 'Function tests',
                  6:'Combinatorial tests', 7:'Playtest', 8:'Collision tests', 9:'Ad hoc tests'}
    
    T12 = data[['T12r1', 'T12r2', 'T12r3', 'T12r4', 'T12r5', 'T12r6', 'T12r7', 'T12r8', 'T12r9', 'T12r10']]
    
    T12_testingsConducted = pd.DataFrame()
    
    for i, row in T12.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['testings_conducted'] = titles
        T12_testingsConducted = T12_testingsConducted.append(row)
    
    T12_testingsConducted['testings_conducted'] = T12_testingsConducted['testings_conducted'].apply(lambda x: x if isinstance(x, list) else [])
    T12_testingsConducted = T12_testingsConducted['testings_conducted']
    
    
    # =============================================================================
    # # for T12a ORDER - testing_time_consumed(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for T12a
    columnDict = {'1': 'Smoke tests', 
                  '2': 'Unit tests',
                  '3': 'Asset validation',
                  '4': 'Performance tests', '5':'Regression tests', '6': 'Function tests',
                  '7':'Combinatorial tests', '8':'Playtest', '9':'Collision tests', '10':'Ad hoc tests',
                  '' :''}
    
    
    T12a = data[['T12a_Orderr1', 'T12a_Orderr2', 'T12a_Orderr3', 'T12a_Orderr4', 'T12a_Orderr5',
                  'T12a_Orderr6', 'T12a_Orderr7', 'T12a_Orderr8', 'T12a_Orderr9', 'T12a_Orderr10']]
                 
    T12a_orders = pd.DataFrame()
    
    for i, row in T12a.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        T12a_orders = T12a_orders.append([result_list])
      
    T12a_orders = T12a_orders.reset_index(drop = True)    
    T12a_orders['order'] = T12a_orders.values.tolist()
    T12a_orders = T12a_orders['order']
    
    
    # =============================================================================
    # # for T12b - automations_in_tests
    # =============================================================================
    # Define the text corresponding to each index for T12b
    columnDict = {0: 'Smoke tests', 1: 'Unit tests', 2: 'Asset validation',
                  3: 'Performance tests', 4:'Regression tests', 5: 'Function tests',
                  6:'Combinatorial tests', 7:'Playtest', 8:'Collision tests', 9:'Ad hoc tests',
                  10:'No automation used in any of these tests'}
    
    T12b = data[['T12br1', 'T12br2', 'T12br3', 'T12br4', 'T12br5', 'T12br6', 'T12br7', 'T12br8', 
                'T12br9', 'T12br10']]
    
    T12b_automationsInTest = pd.DataFrame()
    
    for i, row in T12b.iterrows():
        row_values = row.values.tolist()
        titles = [columnDict[index] for index, value in enumerate(row_values) if value == 1]
        row['automations_in_tests'] = titles
        T12b_automationsInTest = T12b_automationsInTest.append(row)
    
    T12b_automationsInTest['automations_in_tests'] = T12b_automationsInTest['automations_in_tests'].apply(lambda x: x if isinstance(x, list) else [])
    T12b_automationsInTest = T12b_automationsInTest['automations_in_tests']
    
    
    # =============================================================================
    # # DATA & ANALYTICS
    # =============================================================================
    
    # =============================================================================
    # # for DA12 ORDER - data_operation_challenges(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for DA12
    columnDict = {'1':'collection',
                 '2':'cleaning',
                 '3':'merging',
                 '4':'analysis',
                 '5':'visualization',
                  '' :''}
    
    
    DA12 = data[['DA12_Orderr1', 'DA12_Orderr2', 'DA12_Orderr3', 'DA12_Orderr4', 'DA12_Orderr5']]
                 
    DA12_orders = pd.DataFrame()
    
    for i, row in DA12.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        DA12_orders = DA12_orders.append([result_list])
      
    DA12_orders = DA12_orders.reset_index(drop = True)    
    DA12_orders['order'] = DA12_orders.values.tolist()
    DA12_orders = DA12_orders['order']
    
    
    
    # =============================================================================
    # # for DA13 ORDER - data_operation_valuable(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for DA13
    columnDict = {'1':'Player analysis',
                 '2':'Player valuation',
                 '3':'Game design/experience',
                 '4':'Monetization',
                 '5':'User acquisition',
                 '6':'Game performance',
                  '' :''}
    
    DA13 = data[['DA13_Orderr1', 'DA13_Orderr2', 'DA13_Orderr3', 'DA13_Orderr4', 'DA13_Orderr5', 'DA13_Orderr6']]
                 
    DA13_orders = pd.DataFrame()
    
    for i, row in DA13.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        DA13_orders = DA13_orders.append([result_list])
      
    DA13_orders = DA13_orders.reset_index(drop = True)    
    DA13_orders['order'] = DA13_orders.values.tolist()
    DA13_orders = DA13_orders['order']
    
    
    
    # =============================================================================
    # # for DA13a ORDER - data_operation_challenges(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for DA13a
    columnDict = {'1':'Player analysis',
                 '2':'Player valuation',
                 '3':'Game design/experience',
                 '4':'Monetization',
                 '5':'User acquisition',
                 '6':'Game performance',
                  '' :''}
    
    
    DA13a = data[['DA13a_Orderr1', 'DA13a_Orderr2', 'DA13a_Orderr3', 'DA13a_Orderr4', 
                  'DA13a_Orderr5', 'DA13a_Orderr6']]
                 
    DA13a_orders = pd.DataFrame()
    
    for i, row in DA13a.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        DA13a_orders = DA13a_orders.append([result_list])
      
    DA13a_orders = DA13a_orders.reset_index(drop = True)    
    DA13a_orders['order'] = DA13a_orders.values.tolist()
    DA13a_orders = DA13a_orders['order']
    
    
    
    # =============================================================================
    # # for DA15b ORDER - barriers(most_to_least)
    # =============================================================================
    # Define the text corresponding to each index for DA15b
    columnDict = {'1':'Data not readily available',
                 '2':'Data is challenging to utilize',
                 '3':'Challenges in analysis',
                 '4':'Not a culture of making data-driven decisions',
                 '5':'No barries',
                  '' :''}
    
    
    DA15b = data[['DA15b_Orderr1', 'DA15b_Orderr2', 'DA15b_Orderr3', 'DA15b_Orderr4', 'DA15b_Orderr5']]
                 
    DA15b_orders = pd.DataFrame()
    
    for i, row in DA15b.iterrows():
        row = np.asarray(row)
        row = np.where(np.isnan(row), '', row.astype(int).astype(str))
        row = row.tolist()
        rowResulted = [''] * len(row)
        
        for index, value in enumerate(row):
            if value == '1':
                rowResulted[0] = index+1
            elif value == '2':
                rowResulted[1] = index+1
            elif value == '3':
                rowResulted[2] = index+1
            elif value == '4':
                rowResulted[3] = index+1
            elif value == '5':
                rowResulted[4] = index+1
            elif value == '6':
                rowResulted[5] = index+1
            elif value == '7':
                rowResulted[6] = index+1
            elif value == ' ':
                rowResulted[index] = ' '
    
        result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
        
        DA15b_orders = DA15b_orders.append([result_list])
      
    DA15b_orders = DA15b_orders.reset_index(drop = True)    
    DA15b_orders['order'] = DA15b_orders.values.tolist()
    DA15b_orders = DA15b_orders['order']
    
    
    
    
    
    
    #codedValues = {'1':'Studio Management', '2':'Production', '3':'Artist & content creation', 
    #               '4':'Developer & software engineer', '5':'QA & testing', '6':'Data, analytics, monetization', 
    #               '7':'Finance', '8':'Legal & HR', '9':'Events'}
    #
    #DM7_currentRole = DM7Merged.replace({'DM7':codedValues})
    
    cleanedData = data[['record', 'uuid', 'date', 'status', 'dTrack', 'start_date', 'psid', 'LOI', 'dCountry']]
    # Demographics
    cleanedData.loc[:,'company'] = DM1_company
    cleanedData.loc[:,'company_types'] = DM2_companyTypes
    cleanedData.loc[:,'game_produced'] = DM3_gameProduced
    cleanedData.loc[:,'studio_type'] = DM4_studioType
    cleanedData.loc[:,'studio_own_type'] = DM4_ownType 
    cleanedData.loc[:,'titles'] = DM5_titles
    cleanedData.loc[:,'platforms'] = DM6_platforms
    cleanedData.loc[:,'current_role'] = DM7_currentRole
    cleanedData.loc[:,'production_role'] = PL7_productionRole
    cleanedData.loc[:,'other_industry_work'] = DM8_otherIndustryWork
    cleanedData.loc[:,'location_frequency'] = DM9_location_frequency
    cleanedData.loc[:,'your_work_types'] = DM9a_yourWorkTypes
    # =============================================================================
    # #Industry Trends
    # =============================================================================
    codedValues = {'1':'Agree',
                   '2':'Disagree', 
                   '3':'Does not apply to me'}
    
    cleanedData.loc[:,'cost_rising'] = recodeValues(codedValues, 'IT1r1', data)
    cleanedData.loc[:,'from_hypercasual_to_midcore'] = recodeValues(codedValues, 'IT1r2', data)
    cleanedData.loc[:,'player_demand_AA/AAA_game_quality'] = recodeValues(codedValues, 'IT1r3', data)
    cleanedData.loc[:,'cross_platform_multiplayer-studio_support_needed'] = recodeValues(codedValues, 'IT1r4', data)
    cleanedData.loc[:,'use_data_analytics'] = recodeValues(codedValues, 'IT1r5', data)
    cleanedData.loc[:,'live_services_needed'] = recodeValues(codedValues, 'IT1r6', data)
    cleanedData.loc[:,'scarcity_challenges_studio_growth'] = recodeValues(codedValues, 'IT1r7', data)
    cleanedData.loc[:,'industry_trends_challenges(most_to_least)'] = IT1A_orders
    cleanedData.loc[:,'game_engine'] = IT2_gameEngine
    cleanedData.loc[:,'other_game_engine'] = IT2A_other_game_engine
    cleanedData.loc[:,'live_services_title'] = IT3_liveServicesTitle
    cleanedData.loc[:,'cloud_technology_usage'] = IT4_cloudTechnologyUsage
    
    codedValues = {'0':'No',
                   '1':'Yes'}
    cleanedData.loc[:,'performance_concerns'] = recodeValues(codedValues, 'IT4ar1', data)
    cleanedData.loc[:,'cost_concerns'] = recodeValues(codedValues, 'IT4ar2', data)
    cleanedData.loc[:,'reliability_concerns'] = recodeValues(codedValues, 'IT4ar4', data)
    cleanedData.loc[:,'learning_curve_concerns'] = recodeValues(codedValues, 'IT4ar5', data)
    cleanedData.loc[:,'no_internal_expertise'] = recodeValues(codedValues, 'IT4ar6', data)
    cleanedData.loc[:,'no_product_meet_needs'] = recodeValues(codedValues, 'IT4ar7', data)
    cleanedData.loc[:,'no_concerns'] = recodeValues(codedValues, 'IT4ar8', data)
    cleanedData.loc[:,'migrating_to_cloud_concerns(most_to_least)'] = IT4A_orders
    cleanedData.loc[:,'studio_title_for_blockchain'] = IT5_studioTitle
    
    cleanedData.loc[:,'artist_content_creation'] = recodeValues(codedValues, 'IT6r1', data)
    cleanedData.loc[:,'game_engine_programming'] = recodeValues(codedValues, 'IT6r2', data)
    cleanedData.loc[:,'testing_and_QA_processes'] = recodeValues(codedValues, 'IT6r3', data)
    cleanedData.loc[:,'narrative_&_story'] = recodeValues(codedValues, 'IT6r4', data)
    cleanedData.loc[:,'game_design'] = recodeValues(codedValues, 'IT6r5', data)
    cleanedData.loc[:,'intelligent_npcs'] = recodeValues(codedValues, 'IT6r6', data)
    cleanedData.loc[:,'player-generated_content'] = recodeValues(codedValues, 'IT6r7', data)
    cleanedData.loc[:,'audio/language_generation'] = recodeValues(codedValues, 'IT6r8', data)
    cleanedData.loc[:,'audio/language_generation'] = recodeValues(codedValues, 'IT6r8', data)
    cleanedData.loc[:,'AI_replace_employee_aspect-others'] = IT6r9
    cleanedData.loc[:,'impact_by_AI_on_development'] = IT6_orders
    cleanedData.loc[:,'when_AI_replace_employee'] = IT6a_AI_replace_Employee
    
    codedValues = {'1':'Apple',
                 '2':'Orange',
                 '3':'Pear',
                 '4':'Blueberry',
                 '5':'Banana',
                 '6':'None of the above'}
    cleanedData.loc[:,'qualityCheck1'] = recodeValues(codedValues, 'QCHECK1', data)
    
    cleanedData.loc[:,'artist_type'] = A1Merged
    cleanedData.loc[:,'3D_game_content_cost_change'] = A11_costChange3D
    
    cleanedData.loc[:,'reason_of_cost_increase(most_to_least)'] = A11a_orders
    cleanedData.loc[:,'reason_of_cost_decrease(most_to_least)'] = A11b_orders
    
    
    codedValues = {1.0:'Very painful',
                   2.0:'Somewhat painful', 
                   3.0:'Not painful',
                   4.0:'Does not apply to me'}
    cleanedData.loc[:,'collaborative_working'] = recodeValues(codedValues, 'A12r1', data, string = False)
    cleanedData.loc[:,'filetype_conversions'] = recodeValues(codedValues, 'A12r2', data, string = False)
    cleanedData.loc[:,'large_files_download_&_upload'] = recodeValues(codedValues, 'A12r3', data, string = False)
    cleanedData.loc[:,'validating_asset_submission'] = recodeValues(codedValues, 'A12r4', data, string = False)
    cleanedData.loc[:,'managing_large_libraries'] = recodeValues(codedValues, 'A12r5', data, string = False)
    cleanedData.loc[:,'new_content_creation'] = recodeValues(codedValues, 'A12r6', data, string = False)
    
    
    
    codedValues = {1.0:'Use an off-the-shelf tool',
                   2.0:'Built a custom solution', 
                   3.0:'didn’t use this'}
    cleanedData.loc[:,'version_control_sys'] = recodeValues(codedValues, 'A13r1', data, string = False)
    cleanedData.loc[:,'asset_management_sys'] = recodeValues(codedValues, 'A13r2', data, string = False)
    cleanedData.loc[:,'asset_optimization_tools'] = recodeValues(codedValues, 'A13r3', data, string = False)
    
    
    
    codedValues = {1.0:'Very unsatisfied',
                   2.0:'Somewhat unsatisfied', 
                   3.0:'Satisfied',
                   4.0:'Very satisfied',
                   5.0:'Does not apply to me'}
    cleanedData.loc[:,'satisfaction_VCS'] = recodeValues(codedValues, 'A13ar1', data, string = False)
    cleanedData.loc[:,'satisfaction_AMS'] = recodeValues(codedValues, 'A13ar2', data, string = False)
    cleanedData.loc[:,'satisfaction_AOT'] = recodeValues(codedValues, 'A13ar3', data, string = False)
    
    
    
    codedValues = {1.0:'Using in production',
                   2.0:'Experimenting with', 
                   3.0:'Not using but interested',
                   4.0:'Not interested',
                   5.0:'Unaware'}
    cleanedData.loc[:,'multiuser_editing'] = recodeValues(codedValues, 'A14r1', data, string = False)
    cleanedData.loc[:,'markerless_motion_capture'] = recodeValues(codedValues, 'A14r2', data, string = False)
    cleanedData.loc[:,'procedural_editing_tools'] = recodeValues(codedValues, 'A14r3', data, string = False)
    cleanedData.loc[:,'virtual_workstations'] = recodeValues(codedValues, 'A14r4', data, string = False)
    cleanedData.loc[:,'usd-based_pipelines'] = recodeValues(codedValues, 'A14r5', data, string = False)
    cleanedData.loc[:,'neural_rendering'] = recodeValues(codedValues, 'A14r6', data, string = False)
    
    
    
    codedValues = {1.0:'Not valuable at all',
                   2.0:'Not very valuable', 
                   3.0:'Valuable',
                   4.0:'Very valuable',
                   5.0:'Does not apply to me'}
    cleanedData.loc[:,'isValuable_multiuser_editing'] = recodeValues(codedValues, 'A14ar1', data, string = False)
    cleanedData.loc[:,'isValuable_markerless_motion_capture'] = recodeValues(codedValues, 'A14ar2', data, string = False)
    cleanedData.loc[:,'isValuable_procedural_editing_tools'] = recodeValues(codedValues, 'A14ar3', data, string = False)
    cleanedData.loc[:,'isValuable_virtual_workstations'] = recodeValues(codedValues, 'A14ar4', data, string = False)
    cleanedData.loc[:,'isValuable_usd-based_pipelines'] = recodeValues(codedValues, 'A14ar5', data, string = False)
    cleanedData.loc[:,'isValuable_neural_rendering'] = recodeValues(codedValues, 'A14ar6', data, string = False)
    
    
    
    codedValues = {1.0:'Using in production', 
                   2.0:'Experimenting with', 
                   3.0:'Not using', 
                   4.0:'Not interested'}
    cleanedData.loc[:,'storyboard_illustration-2d'] = recodeValues(codedValues, 'A16r1', data, string = False)
    cleanedData.loc[:,'2d_textures'] = recodeValues(codedValues, 'A16r2', data, string = False)
    cleanedData.loc[:,'untextured_3d_mesh'] = recodeValues(codedValues, 'A16r3', data, string = False)
    cleanedData.loc[:,'textured_3d_model'] = recodeValues(codedValues, 'A16r4', data, string = False)
    cleanedData.loc[:,'scene_generation'] = recodeValues(codedValues, 'A16r5', data, string = False)
    cleanedData.loc[:,'generative_AI-others'] = A16r6
    
    
    cleanedData.loc[:,'t_effiency_slider-storyboard_illustration-2d'] = data['A16ar1']
    cleanedData.loc[:,'t_effiency_slider-2d_textures'] = data['A16ar2']
    cleanedData.loc[:,'t_effiency_slider-untextured_3d_mesh'] = data['A16ar3']
    cleanedData.loc[:,'t_effiency_slider-textured_3d_model'] = data['A16ar4']
    cleanedData.loc[:,'t_effiency_slider-scene_generation'] =  data['A16ar5']
    cleanedData.loc[:,'t_effiency_slider-generative_AI-others'] = data['A16ar6']
    
    
    cleanedData.loc[:,'useful_AI_tool'] = data['A16b']
    
    # =============================================================================
    # #Dev & Engineering
    # =============================================================================
    codedValues = {1.0:'Very painful', 
                   2.0:'Somewhat painful', 
                   3.0:'Not painful', 
                   4.0:'Does not apply to me'}
    cleanedData.loc[:,'time_to_compile_codes'] = recodeValues(codedValues, 'DE11r1', data, string = False)
    cleanedData.loc[:,'maintainance'] = recodeValues(codedValues, 'DE11r2', data, string = False)
    cleanedData.loc[:,'upgrading_pipelines'] = recodeValues(codedValues, 'DE11r3', data, string = False)
    cleanedData.loc[:,'multi-platform_development'] = recodeValues(codedValues, 'DE11r4', data, string = False)
    cleanedData.loc[:,'building_custom_backend'] = recodeValues(codedValues, 'DE11r5', data, string = False)
    
    
    
    codedValues = {1.0:'0-5 minutes', 
                   2.0:'5-10 minutes', 
                   3.0:'10-30 minutes', 
                   4.0:'30 minutes or more'}
    cleanedData.loc[:,'scratch_build_time'] = recodeValues(codedValues, 'DE12a', data, string = False)
    
    
    
    codedValues = {1.0:'Less than 1 minute', 
                   2.0:'1-5 minutes', 
                   3.0:'5-10 minutes', 
                   4.0:'More than 10 minutes'}
    cleanedData.loc[:,'iterative_build_time'] = recodeValues(codedValues, 'DE12b', data, string = False)
    
    
    cleanedData.loc[:, 'pipeline_tools'] = DE16_pipelineTool
    
    
    codedValues = {0.0:'No', 
                   1.0:'Yes'}
    cleanedData.loc[:,'iterative_build_time'] = recodeValues(codedValues, 'DE12b', data, string = False)
    
    cleanedData.loc[:,'building_pipeline_problems'] = DE16a_pipelineProblems
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No'}
    cleanedData.loc[:,'satisfied_with_pipeline'] = recodeValues(codedValues, 'DE16b', data, string = False)
    cleanedData.loc[:,'use_devops_model'] = recodeValues(codedValues, 'DE17', data, string = False)
    
    
    cleanedData.loc[:,'practices_implemented'] = DE17a_practicesImplemented
    
    
    codedValues_modularity = {1.0:'Monolithic', 
                   2.0:'Monolithic with a few modular services',
                   3.0:'Monolithic but most services are modular',
                   4.0:'Entirely modular'}
    cleanedData.loc[:,'game_engine_modularity'] = recodeValues(codedValues, 'DE18', data, string = False)
    
    codedValues = {1.0:'Yes', 
                   2.0:'No'}
    
    cleanedData.loc[:,'modularity_desired?'] = recodeValues(codedValues, 'DE18a', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'Sometimes',
                   3.0:'No'}
    
    cleanedData.loc[:,'avoid_software_updates?'] = recodeValues(codedValues, 'DE18b', data, string = False)
    
    
    cleanedData.loc[:,'gameplay_code_modularity'] = recodeValues(codedValues_modularity, 'DE18c', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No'}
    
    cleanedData.loc[:,'more_modularity_beneficial?'] = recodeValues(codedValues, 'DE18d', data, string = False)
    
    
    cleanedData.loc[:,'game_build_modularity'] = recodeValues(codedValues_modularity, 'DE18e', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No',
                   3.0:'N/A - Does not apply to me'}
    
    cleanedData.loc[:,'monolithic_make_difficulty?'] = recodeValues(codedValues, 'DE18f', data, string = False)
    
    
    codedValues = {1.0:'Use off the shelf solutions', 
                   2.0:'Mostly off the shelf with some custom solutions',
                   3.0:'Mostly custom with some off the shelf solutions',
                   4.0:'Entirely build our own'}
    
    cleanedData.loc[:,'own_vs_solutions'] = recodeValues(codedValues, 'DE20', data, string = False)
    
    
    codedValues = {1.0:'Off the shelf tool', 
                   2.0:'Custom built solutions', 
                   3.0:'Not applicable'}
    cleanedData.loc[:,'economy'] = recodeValues(codedValues, 'DE20ar1', data, string = False)
    cleanedData.loc[:,'game_server_hosting'] = recodeValues(codedValues, 'DE20ar2', data, string = False)
    cleanedData.loc[:,'matchmaking'] = recodeValues(codedValues, 'DE20ar3', data, string = False)
    cleanedData.loc[:,'social_features'] = recodeValues(codedValues, 'DE20ar4', data, string = False)
    cleanedData.loc[:,'game_and_player_data'] = recodeValues(codedValues, 'DE20ar5', data, string = False)
    cleanedData.loc[:,'liveops'] = recodeValues(codedValues, 'DE20ar6', data, string = False)
    
    
    
    codedValues = {1.0:'Not satisfied at all', 
                   2.0:'Some dissatisfaction', 
                   3.0:'Satisfied',
                   4.0:'Very satisfied',
                   5.0:'Does not apply to me'}
    cleanedData.loc[:,'satisfaction_economy'] = recodeValues(codedValues, 'DE20br1', data, string = False)
    cleanedData.loc[:,'satisfaction_game_server_hosting'] = recodeValues(codedValues, 'DE20br2', data, string = False)
    cleanedData.loc[:,'satisfaction_matchmaking'] = recodeValues(codedValues, 'DE20br3', data, string = False)
    cleanedData.loc[:,'satisfaction_social_features'] = recodeValues(codedValues, 'DE20br4', data, string = False)
    cleanedData.loc[:,'satisfaction_game_and_player_data'] = recodeValues(codedValues, 'DE20br5', data, string = False)
    cleanedData.loc[:,'satisfaction_liveops'] = recodeValues(codedValues, 'DE20br6', data, string = False)
    
    
    codedValues = {1.0:'Off the shelf tool', 
                   2.0:'Custom software', 
                   3.0:'Don’t use but interested',
                   4.0:'Not interested'}
    cleanedData.loc[:,'hot_reloading_tools'] = recodeValues(codedValues, 'DE21r1', data, string = False)
    cleanedData.loc[:,'build_acceleration_solutions'] = recodeValues(codedValues, 'DE21r2', data, string = False)
    cleanedData.loc[:,'virtual_workstations'] = recodeValues(codedValues, 'DE21r3', data, string = False)
    cleanedData.loc[:,'cloud_pipelines'] = recodeValues(codedValues, 'DE21r4', data, string = False)
    cleanedData.loc[:,'testing_automation'] = recodeValues(codedValues, 'DE21r5', data, string = False)
    
    
    
    # =============================================================================
    # #Testing
    # =============================================================================
    
    codedValues = {1.0:'Multiple per day', 
                   2.0:'Daily',
                   3.0:'Weekly',
                   4.0:'Monthly',
                   5.0:'Every few months'}
    
    cleanedData.loc[:,'new_version_frequency'] = recodeValues(codedValues, 'T11', data, string = False)
    
    
    codedValues = {1.0:'None', 
                   2.0:'1-5 minutes',
                   3.0:'5-15 minutes',
                   4.0:'15-30 minutes',
                   5.0:'30 minutes to 1 hour',
                   6.0:'1-2 hours',
                   7.0:'2 or more hours'}
    
    cleanedData.loc[:,'downtime_experienced'] = recodeValues(codedValues, 'T11a', data, string = False)
    
    
    codedValues = {1.0:'Mostly using development builds', 
                   2.0:'Mostly using release builds',
                   3.0:'We use a good balance of both'}
    
    cleanedData.loc[:,'how_builds_tested'] = recodeValues(codedValues, 'T11b', data, string = False)
    
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No'}
    
    cleanedData.loc[:,'is_game_tested_frequently'] = recodeValues(codedValues, 'T11c', data, string = False)
    cleanedData.loc[:,'why_not_tested_frequently'] = T11d_whyNot
    
    cleanedData.loc[:,'testings_conducted'] = T12_testingsConducted
    
    codedValues = {0.0:'No',
                   1.0:'Yes'}
    cleanedData.loc[:,'smoke_tests'] = recodeValues(codedValues, 'T12ar1', data)
    cleanedData.loc[:,'unit_tests'] = recodeValues(codedValues, 'T12ar2', data)
    cleanedData.loc[:,'asset_validations'] = recodeValues(codedValues, 'T12ar3', data)
    cleanedData.loc[:,'performance_tests'] = recodeValues(codedValues, 'T12ar4', data)
    cleanedData.loc[:,'regression_tests'] = recodeValues(codedValues, 'T12ar5', data)
    cleanedData.loc[:,'function_tests'] = recodeValues(codedValues, 'T12ar6', data)
    cleanedData.loc[:,'combinatorial_tests'] = recodeValues(codedValues, 'T12ar7', data)
    cleanedData.loc[:,'playtest'] = recodeValues(codedValues, 'T12ar8', data)
    cleanedData.loc[:,'collision_tests'] = recodeValues(codedValues, 'T12ar9', data)
    cleanedData.loc[:,'ad_hoc_tests'] = recodeValues(codedValues, 'T12ar10', data)
    cleanedData.loc[:,'testing_time_consumed(most_to_least)'] = T12a_orders
    
    cleanedData.loc[:,'automations_in_tests'] = T12b_automationsInTest
    
    
    codedValues = {0.0:'Off the shelf tool',
                   1.0:'Custom tool'}
    cleanedData.loc[:,'smoke_tests-toolUsed'] = recodeValues(codedValues, 'T12dr1', data)
    cleanedData.loc[:,'unit_tests-toolUsed'] = recodeValues(codedValues, 'T12dr2', data)
    cleanedData.loc[:,'asset_validations-toolUsed'] = recodeValues(codedValues, 'T12dr3', data)
    cleanedData.loc[:,'performance_tests-toolUsed'] = recodeValues(codedValues, 'T12dr4', data)
    cleanedData.loc[:,'regression_tests-toolUsed'] = recodeValues(codedValues, 'T12dr5', data)
    cleanedData.loc[:,'function_tests-toolUsed'] = recodeValues(codedValues, 'T12dr6', data)
    cleanedData.loc[:,'combinatorial_tests-toolUsed'] = recodeValues(codedValues, 'T12dr7', data)
    cleanedData.loc[:,'playtest-toolUsed'] = recodeValues(codedValues, 'T12dr8', data)
    cleanedData.loc[:,'collision_tests-toolUsed'] = recodeValues(codedValues, 'T12dr9', data)
    cleanedData.loc[:,'ad_hoc_tests-toolUsed'] = recodeValues(codedValues, 'T12dr10', data)
    
    
    codedValues = {1.0:'Always', 
                   2.0:'Frequently',
                   3.0:'Sometimes',
                   4.0:'Rarely',
                   5.0:'Never'}
    cleanedData.loc[:,'QA_before_release'] = recodeValues(codedValues, 'T13', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No',
                   3.0:'Does not apply to me'}
    cleanedData.loc[:,'QA_part_of_pipeline'] = recodeValues(codedValues, 'T13a', data, string = False)
    
    
    codedValues = {1.0:'Always', 
                   2.0:'Sometimes',
                   3.0:'Never'}
    cleanedData.loc[:,'smoke_testing'] = recodeValues(codedValues, 'T13b', data, string = False)
    cleanedData.loc[:,'asset_validation'] = recodeValues(codedValues, 'T13c', data, string = False)
    
    
    codedValues = {1.0:'Increase in complexity', 
                   2.0:'Decrease in complexity',
                   3.0:'No change'}
    cleanedData.loc[:,'QA_change_in_future'] = recodeValues(codedValues, 'T14', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No'}
    cleanedData.loc[:,'resource_QA_in_future'] = recodeValues(codedValues, 'T14a', data, string = False)
    
    
    
    # =============================================================================
    # #Data & Analytics
    # =============================================================================
    
    
    codedValues = {1.0:'We collect too much data', 
                   2.0:'We collect just what we need',
                   3.0:'We collect too little data'}
    cleanedData.loc[:,'data_collection_practices'] = recodeValues(codedValues, 'DA11', data, string = False)
    
    
    codedValues = {1.0:'Yes, we use and merge datasets', 
                   2.0:'Yes, we have visibility and access',
                   3.0:'No, data is siloed between teams',
                   4.0:'We don’t have other titles, teams, or studios'}
    cleanedData.loc[:,'other_data_usage'] = recodeValues(codedValues, 'DA11a', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No, but interested',
                   3.0:'No, and not interested'}
    cleanedData.loc[:,'3rd_party_data_usage'] = recodeValues(codedValues, 'DA11b', data, string = False)
    
    
    codedValues = {1.0:'No benefit', 
                   2.0:'Not very beneficial',
                   3.0:'Some benefit',
                   4.0:'Very beneficial'}
    cleanedData.loc[:,'other_data_sources_beneficial'] = recodeValues(codedValues, 'DA11c', data, string = False)
    
    
    codedValues = {1.0:'No benefit', 
                   2.0:'Not very beneficial',
                   3.0:'Some benefit',
                   4.0:'Very beneficial'}
    cleanedData.loc[:,'other_data_sources_beneficial'] = recodeValues(codedValues, 'DA11c', data, string = False)
    
    
    codedValues = {0.0:'No',
                   1.0:'Yes'}
    cleanedData.loc[:,'collection'] = recodeValues(codedValues, 'DA12r1', data)
    cleanedData.loc[:,'cleaning'] = recodeValues(codedValues, 'DA12r2', data)
    cleanedData.loc[:,'merging'] = recodeValues(codedValues, 'DA12r3', data)
    cleanedData.loc[:,'analysis'] = recodeValues(codedValues, 'DA12r4', data)
    cleanedData.loc[:,'visualization'] = recodeValues(codedValues, 'DA12r5', data)
    cleanedData.loc[:,'data_operation_challenges(most_to_least)'] = DA12_orders
    
    
    codedValues = {1.0:'None', 
                   2.0:'1',
                   3.0:'2-4',
                   4.0:'5-7',
                   5.0:'8 or more'}
    cleanedData.loc[:,'data_analytics_tools'] = recodeValues(codedValues, 'DA12a', data, string = False)
    
    
    codedValues = {1.0:'Reduce cost and complexity', 
                   2.0:'Improve speed and quality',
                   3.0:'Enable us to explore more innovative analyses',
                   4.0:'It would not be beneficial'}
    cleanedData.loc[:,'simplifying_pipeline_beneficial'] = recodeValues(codedValues, 'DA12b', data, string = False)
    
    
    
    codedValues = {0.0:'No',
                   1.0:'Yes'}
    cleanedData.loc[:,'V_player_analysis'] = recodeValues(codedValues, 'DA13r1', data)
    cleanedData.loc[:,'V_player_valuation'] = recodeValues(codedValues, 'DA13r2', data)
    cleanedData.loc[:,'V_game_design/experience'] = recodeValues(codedValues, 'DA13r3', data)
    cleanedData.loc[:,'V_monetization'] = recodeValues(codedValues, 'DA13r4', data)
    cleanedData.loc[:,'V_user_acquisition'] = recodeValues(codedValues, 'DA13r5', data)
    cleanedData.loc[:,'V_game_performance'] = recodeValues(codedValues, 'DA13r6', data)
    cleanedData.loc[:,'valuable_analysis(most_to_least)'] = DA13_orders
    
    
    codedValues = {0.0:'No',
                   1.0:'Yes'}
    cleanedData.loc[:,'C_player_analysis'] = recodeValues(codedValues, 'DA13ar1', data)
    cleanedData.loc[:,'C_player_valuation'] = recodeValues(codedValues, 'DA13ar2', data)
    cleanedData.loc[:,'C_game_design/experience'] = recodeValues(codedValues, 'DA13ar3', data)
    cleanedData.loc[:,'C_monetization'] = recodeValues(codedValues, 'DA13ar4', data)
    cleanedData.loc[:,'C_user_acquisition'] = recodeValues(codedValues, 'DA13ar5', data)
    cleanedData.loc[:,'C_game_performance'] = recodeValues(codedValues, 'DA13ar6', data)
    cleanedData.loc[:,'challenging_analysis(most_to_least)'] = DA13a_orders
    
    
    codedValues = {1.0:'General BI tool (Tableau)', 
                   2.0:'Games specific toolkit (Unity Analytics)',
                   3.0:'Custom built toolkit',
                   4.0:'None'}
    cleanedData.loc[:,'BI_tool_usage'] = recodeValues(codedValues, 'DA13b', data, string = False)
    
    
    codedValues = {1.0:'1 - Not at all', 
                   2.0:'2',
                   3.0:'3',
                   4.0:'4',
                   5.0:'5 - All needs are covered'}
    cleanedData.loc[:,'BI_tool_meet_needs'] = recodeValues(codedValues, 'DA13c', data, string = False)
    
    
    codedValues = {1.0:'No significant use of data analytics', 
                   2.0:'Limited use of data for ad hoc reporting',
                   3.0:'Regular use to inform decision making',
                   4.0:'Advanced use in driving dynamic gameplay optimization'}
    cleanedData.loc[:,'how_studio_use_DA'] = recodeValues(codedValues, 'DA14', data, string = False)
    
    
    codedValues = {1.0:'Yes', 
                   2.0:'No, but interested',
                   3.0:'No, and not interested'}
    cleanedData.loc[:,'use_CRM_platform'] = recodeValues(codedValues, 'DA14b', data, string = False)
    
    
    codedValues = {1.0:'Our title has a dedicated data team', 
                   2.0:'Our title shares data resources with others',
                   3.0:'We use a third party for our data',
                   4.0:'We don’t have a data team'}
    cleanedData.loc[:,'how_teams_organized'] = recodeValues(codedValues, 'DA15', data, string = False)
    
    
    
    codedValues = {1.0:'Dedicated data teams per title', 
                   2.0:'Centralized data teams across titles',
                   3.0:'Outsourced data teams'}
    cleanedData.loc[:,'effective_model_for_teams'] = recodeValues(codedValues, 'DA15a', data, string = False)
    
    
    
    codedValues = {0.0:'No',
                   1.0:'Yes'}
    cleanedData.loc[:,'data_not_available'] = recodeValues(codedValues, 'DA15br1', data)
    cleanedData.loc[:,'data_challenging_to_utilize'] = recodeValues(codedValues, 'DA15br2', data)
    cleanedData.loc[:,'challenges_in_analysis'] = recodeValues(codedValues, 'DA15br3', data)
    cleanedData.loc[:,'not_a_culture_of_making_data-driven_decisions'] = recodeValues(codedValues, 'DA15br4', data)
    cleanedData.loc[:,'no_barriers'] = recodeValues(codedValues, 'DA15br5', data)
    cleanedData.loc[:,'barriers_in_decision_making(most_to_least)'] = DA15b_orders
    
    
    """# SECTION: Production & LiveOps Section [ASK IF DM7=2]"""
    
    # PL8r1 to PL8r5
    # List of columns to replace values
    merged_column = ['PL8r1', 'PL8r2', 'PL8r3', 'PL8r4', 'PL8r5']
    
    # Create a new DataFrame to store the replaced columns
    PL8r_df = pd.DataFrame()
    columName = ['game_art', 'game_programming', 'game_design', 'software_engineering', 'testing_&_QA']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Yes', '0.0': 'No'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        PL8r_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    PL8r_df.head()
    
    ### PL8_Orderr1 to PL8_Orderr5
    columnDict = {'1':'Game Art ', 
                  '2':'Game Programming ',
                  '3':'Game Design', 
                  '4':'Software Engineering ',
                  '5':'Testing & QA',
                  '' :''}
    
    PL8 = data[['PL8_Orderr1', 'PL8_Orderr2', 'PL8_Orderr3', 'PL8_Orderr4',
                 'PL8_Orderr5']]
    
    PL8_orders = pd.DataFrame()
    
    for i, row in PL8.iterrows():
      row = np.asarray(row)
      row = np.where(np.isnan(row), '', row.astype(int).astype(str))
      row = row.tolist()
      rowResulted = [''] * len(row)
    
      for index, value in enumerate(row):
          if value == '1':
              rowResulted[0] = index+1
          elif value == '2':
              rowResulted[1] = index+1
          elif value == '3':
              rowResulted[2] = index+1
          elif value == '4':
              rowResulted[3] = index+1
          elif value == '5':
              rowResulted[4] = index+1
          elif value == ' ':
              rowResulted[index] = ' '
      result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
    
      PL8_orders.at[i, "struggle_to_deliver_content(most to least)"] = ', '.join(result_list)
    
    PL8_orders.head()
    
    # PL8a
    
    PL8a = data[['PL8a']]
    merged_column = PL8a['PL8a'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Never (0% of the time)', '2.0':'Rarely (Less than 5% of the time)', '3.0':'Sometimes (5% to less than 50% of the time)', '4.0':'Often (50% to less than 80% of the time)', '5.0':'Almost always (80% of the time or more)'}
    
    PL8a_company = DM1Merged.replace({'PL8a':codedValues})
    PL8a_company.rename(columns={'PL8a': 'teams_exceeding_estimates'}, inplace=True)
    PL8a_company.head()
    
    # PL8b
    PL8b = data[['PL8b']]
    merged_column = PL8b['PL8b'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Meeting short term deadlines', '2.0':'Preventing long term technical debt'}
    
    PL8b_company = DM1Merged.replace({'PL8b':codedValues})
    PL8b_company.rename(columns={'PL8b': 'prioritization'}, inplace=True)
    PL8b_company.head()
    
    # PL9
    PL9 = data[['PL9']]
    merged_column = PL9['PL9'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Very well suited, we are able to deliver live services without any changes or new tools', '2.0':'Moderately well suited, small improvements could be made', '3.0':'Not well suited, it has been challenging to deliver live services without major changes'}
    
    PL9_company = DM1Merged.replace({'PL9':codedValues})
    PL9_company.rename(columns={'PL9': 'production_piplines_and_infrastructure'}, inplace=True)
    PL9_company.head()
    
    # PL9a
    PL9a = data[['PL9a']]
    merged_column = PL9a['PL9a'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Yes, we were able to address both', '2.0':'Yes, we were able to refactor technical debt', '3.0':'Yes, we were able to optimize release pipelines', '4.0':'No, we were not able to do either'}
    
    PL9a_company = DM1Merged.replace({'PL9a':codedValues})
    PL9a_company.rename(columns={'PL9a':'post-launch_optimization_ffforts_OR_post-launch_technical_debt_refactoring'}, inplace=True)
    PL9a_company.head()
    
    # PL9b
    PL9b = data[['PL9b']]
    merged_column = PL9b['PL9b'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Producing content up to launch', '2.0':'Producing content post-launch', '3.0':'I only worked on one (base game production or live-service)'}
    
    PL9b_company = DM1Merged.replace({'PL9b':codedValues})
    PL9b_company.rename(columns={'PL9b':'pre-launch_difficulty_AND_post-launch_difficulty'}, inplace=True)
    PL9b_company.head()
    
    # PL10
    PL10 = data[['PL10']]
    merged_column = PL10['PL10'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Almost always', '2.0':'Sometimes', '3.0':'Rarely', '4.0':'Never'}
    
    PL10_company = DM1Merged.replace({'PL10':codedValues})
    PL10_company.rename(columns={'PL10':'missed_gameplay_defects'}, inplace=True)
    PL10_company.head()
    
    # PL10a
    PL10a = data[['PL10a']]
    merged_column = PL10a['PL10a'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Yes, too much', '2.0':'Yes, just right', '3.0':'No, not enough'}
    
    PL10a_company = DM1Merged.replace({'PL10a':codedValues})
    PL10a_company.rename(columns={'PL10a':'QA_time_&_resources_commitment'}, inplace=True)
    PL10a_company.head()
    
    # PL11
    PL11 = data[['PL11']]
    merged_column = PL11['PL11'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Daily', '2.0':'Weekly', '3.0':'Bimonthly/Twice a month', '4.0':'Monthly', '5.0':'Quarterly', '6.0':'Less than quarterly'}
    
    PL11_company = DM1Merged.replace({'PL11':codedValues})
    PL11_company.rename(columns={'PL11':'live_service_update_frequency'}, inplace=True)
    PL11_company.head()
    
    ## PL11a
    PL11a = data[['PL11a']]
    merged_column = PL11a['PL11a'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Daily', '2.0':'Weekly', '3.0':'Bimonthly/Twice a month', '4.0':'Monthly', '5.0':'Quarterly', '6.0':'Less than quarterly'}
    
    PL11a_company = DM1Merged.replace({'PL11a':codedValues})
    PL11a_company.rename(columns={'PL11a':'desired_update_frequency'}, inplace=True)
    PL11a_company.head()
    
    ## PL11b
    PL11b = data[['PL11b']]
    merged_column = PL11b['PL11b'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Daily', '2.0':'Weekly', '3.0':'Bimonthly/Twice a month', '4.0':'Monthly', '5.0':'Quarterly', '6.0':'Less than quarterly'}
    
    PL11b_company = DM1Merged.replace({'PL11b':codedValues})
    PL11b_company.rename(columns={'PL11b':'patch_install_frequency'}, inplace=True)
    PL11b_company.head()
    
    # PL11c
    PL11c = data[['PL11c']]
    merged_column = PL11c['PL11c'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Significant downtime', '2.0':'Some downtime', '3.0':'Minimal downtime', '4.0':'No downtime'}
    
    PL11c_company = DM1Merged.replace({'PL11c':codedValues})
    PL11c_company.rename(columns={'PL11c':'downtime_with_updates'}, inplace=True)
    PL11c_company.head()
    
    ## PL11d
    PL11d = data[['PL11d']]
    merged_column = PL11d['PL11d'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Less than 1%', '2.0':'1%-5%', '3.0':'More than 5%', '4.0':'Not applicable'}
    
    PL11d_company = DM1Merged.replace({'PL11d':codedValues})
    PL11d_company.rename(columns={'PL11d':'downtime_revenue_loss'}, inplace=True)
    PL11d_company.head()
    
    # PL11e
    PL11e = data[['PL11e']]
    merged_column = PL11e['PL11e'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Almost always', '2.0':'Sometimes', '3.0':'Rarely', '4.0':'Never'}
    
    PL11e_company = DM1Merged.replace({'PL11e':codedValues})
    PL11e_company.rename(columns={'PL11e':'patch_failure_frequency'}, inplace=True)
    PL11e_company.head()
    
    # PL12r1 to PL12r3
    
    # List of columns to replace values
    merged_column = ['PL12r1', 'PL12r2', 'PL12r3']  # Add more column names as needed
    
    # Create a new DataFrame to store the replaced columns
    PL12r_df = pd.DataFrame()
    
    columName = ['identification_speed:outage ','identification_speed:bug','identification_speed:logic/gameplay_issue']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': '<1 hour', '2.0': '<1 day', '3.0':'1 to less than 3 days', '4.0':'3 to less than 7 days', '5.0': '7 to less than 30 days', '6.0':'30 days or more'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        PL12r_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    PL12r_df.head()
    
    # PL12ar1 to PL12ar3
    
    # List of columns to replace values
    merged_column = ['PL12ar1', 'PL12ar2', 'PL12ar3']  # Add more column names as needed
    
    # Create a new DataFrame to store the replaced columns
    PL12ar_df = pd.DataFrame()
    
    columName = ['response_time:outage','response_time:bug','response_time:logic/gameplay_issue']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': '<1 hour', '2.0': '<1 day', '3.0':'1 to less than 3 days', '4.0':'3 to less than 7 days', '5.0': '7 to less than 30 days', '6.0':'30 days or more'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        PL12ar_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    PL12ar_df.head()
    
    
    
    """# SECTION Studio Management [DM7=1]
    
    ### SM11
    """
    
    # SM11
    
    SM11 = data[['SM11']]
    merged_column = SM11['SM11'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1.0':'Less than $1M USD', '2.0':'$1M USD to less than $5M USD', '3.0':'$5M USD to less than $10M USD', '4.0':'$10M USD to less than $50M USD', '5.0':'$50M USD to less than $150M USD', '6.0': '$150M USD +'}
    
    SM11_company = DM1Merged.replace({'SM11':codedValues})
    SM11_company.rename(columns={'SM11': 'budget'}, inplace=True)
    SM11_company.head()
    
    # SM11ar 1 to 7
    
    # List of columns to replace values
    merged_column = ['SM11ar1', 'SM11ar2', 'SM11ar3', 'SM11ar4', 'SM11ar5', 'SM11ar6', 'SM11ar7']  # Add more column names as needed
    
    # Create a new DataFrame to store the replaced columns
    SM11ar_df = pd.DataFrame()
    
    columName = ['spending:game_art','spending:game_programming','spending:game_design', 'spending:software_engineering', 
                 'spending:testing_&_QA', 'spending:data_analytics ', 'spending:other']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Less than 10%', '2.0': '10%-19%', '3.0':'20%-29%', '4.0':'30%-39%', '5.0': '40%-49%', '6.0':'50%-59%', '7.0':'60%-69%', '8.0':'70%-79%','9.0':'80%-89%', '10.0':'90%-99%', '11.0':'100%'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        SM11ar_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    SM11ar_df.head()
    
    """One column (dSM11afl) is skipped in between"""
    
    # SM11b
    # List of columns to replace values
    merged_column = ['SM11br1', 'SM11br2', 'SM11br3', 'SM11br4', 'SM11br5', 'SM11br6']  # Add more column names as needed
    
    # Create a new DataFrame to store the replaced columns
    SM11b_df = pd.DataFrame()
    
    columName = ['budget_change:game_art','budget_change:game_programming','budget_change:game_design', 'budget_change:software_engineering', 
                 'budget_change:testing_&_QA', 'budget_change:data_analytics']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Significantly decrease', '2.0': 'Slightly decrease', '3.0':'Neither', '4.0':'Slightly increase', '5.0': 'Significantly increase'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        SM11b_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    SM11b_df.head()
    
    # SM11c
    
    SM11c = data[['SM11c']]
    
    merged_column = SM11c['SM11c'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'0% to less than 25% ', '2.0':'25% to less than 50%', '3.0':'50% to less than 75%', '4.0':'75% to less than 100%', '5.0':'100% to less than 200%', '6.0':'200%+'}
    
    SM11c_company = DM1Merged.replace({'SM11c':codedValues})
    SM11c_company.rename(columns={'SM11c': 'first_year_gross_income(%)'}, inplace=True)
    SM11c_company.head()
    
    # SM12
    
    SM12 = data[['SM12']]
    
    merged_column = SM12['SM12'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Yes, it’s my biggest challenge', '2.0':'Yes, it’s a major challenge', '3.0':'Yes, it’s a minor challenge', '4.0':'No, we don’t struggle with hiring talent'}
    
    SM12_company = DM1Merged.replace({'SM12':codedValues})
    SM12_company.rename(columns={'SM12': 'hiring_is_challanging?'}, inplace=True)
    SM12_company.head()
    
    # SM12 ar1 to ar7
    
    # List of columns to replace values
    merged_column = ['SM12ar1', 'SM12ar2', 'SM12ar3', 'SM12ar4', 'SM12ar5', 'SM12ar6', 'SM12ar7']
    
    # Create a new DataFrame to store the replaced columns
    SM12_df = pd.DataFrame()
    columName = ['artist:hire', 'engine_programmers:hire', 'designers:hire', 'software_engineers:hire', 'producers:hire', 
                 'testers:hire', 'data_analytics:hire']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Yes', '0.0': 'No'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        SM12_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    SM12_df.head()
    
    # SM12a _Orderr1 to 7
    
    columnDict = {'1':'Artists', 
                  '2':'Engine programmers',
                  '3':'Designers', 
                  '4':'Software engineers',
                  '5':'Producers',
                  '6': 'Testers',
                  '7': 'Data analytics',
                  '' :''}
    
    SM12a = data[['SM12a_Orderr1', 'SM12a_Orderr2', 'SM12a_Orderr3', 'SM12a_Orderr4',
                 'SM12a_Orderr5','SM12a_Orderr6','SM12a_Orderr7']]
    
    SM12a_orders = pd.DataFrame()
    
    for i, row in SM12a.iterrows():
      row = np.asarray(row)
      row = np.where(np.isnan(row), '', row.astype(int).astype(str))
      row = row.tolist()
      rowResulted = [''] * len(row)
    
      for index, value in enumerate(row):
          if value == '1':
              rowResulted[0] = index+1
          elif value == '2':
              rowResulted[1] = index+1
          elif value == '3':
              rowResulted[2] = index+1
          elif value == '4':
              rowResulted[3] = index+1
          elif value == '5':
              rowResulted[4] = index+1
          elif value == '6':
              rowResulted[5] = index+1
          elif value == '7':
              rowResulted[6] = index+1
          elif value == ' ':
              rowResulted[index] = ' '
      result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
    
      SM12a_orders.at[i, "skillsets_difficult_to_hire(most to least)"] = ', '.join(result_list)
    
    SM12a_orders.head()
    
    # SM12 br1 to br7
    
    # List of columns to replace values
    merged_column = ['SM12br1', 'SM12br2', 'SM12br3', 'SM12br4', 'SM12br5', 'SM12br6', 'SM12br7']
    
    # Create a new DataFrame to store the replaced columns
    SM12b_df = pd.DataFrame()
    columName = ['artist:cost', 'developers:cost', 'designers:cost', 'software_engineers:cost', 
                 'producers:cost', 'testers:cost', 'data_analytics:cost']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Yes', '0.0': 'No'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        SM12b_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    SM12b_df.head()
    
    # SM12b _Orderr1 to 7
    
    columnDict = {'1':'Artists', 
                  '2':'Developers',
                  '3':'Designers', 
                  '4':'Software engineers',
                  '5':'Producers',
                  '6': 'Testers',
                  '7': 'Data analytics',
                  '' :''}
    
    SM12a = data[['SM12b_Orderr1', 'SM12b_Orderr2', 'SM12b_Orderr3', 'SM12b_Orderr4',
                 'SM12b_Orderr5','SM12b_Orderr6','SM12b_Orderr7']]
    
    SM12b_orders = pd.DataFrame()
    
    for i, row in SM12a.iterrows():
      row = np.asarray(row)
      row = np.where(np.isnan(row), '', row.astype(int).astype(str))
      row = row.tolist()
      rowResulted = [''] * len(row)
    
      for index, value in enumerate(row):
          if value == '1':
              rowResulted[0] = index+1
          elif value == '2':
              rowResulted[1] = index+1
          elif value == '3':
              rowResulted[2] = index+1
          elif value == '4':
              rowResulted[3] = index+1
          elif value == '5':
              rowResulted[4] = index+1
          elif value == '6':
              rowResulted[5] = index+1
          elif value == '7':
              rowResulted[6] = index+1
          elif value == ' ':
              rowResulted[index] = ' '
      result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
    
      SM12b_orders.at[i, "skillsets_costly_to_hire(most to least)"] = ', '.join(result_list)
    
    SM12b_orders.head()
    
    # SM12c
    SM12c = data[['SM12c']]
    
    merged_column = SM12c['SM12c'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Not at all', '2.0':'Yes, but not often', '3.0':'Yes, often', '4.0':'All the time', '5.0':'Not applicable'}
    
    SM12c_company = DM1Merged.replace({'SM12c':codedValues})
    SM12c_company.rename(columns={'SM12c': 'burnout_experience?'}, inplace=True)
    SM12c_company.head()
    
    # SM12dr1 to SM12dr8oe
    
    # List of columns to replace values
    merged_column = ['SM12dr1', 'SM12dr2', 'SM12dr3', 'SM12dr4', 'SM12dr5', 'SM12dr6', 'SM12dr7']
    
    # Create a new DataFrame to store the replaced columns
    SM12dr_df = pd.DataFrame()
    columName = ['paying_higher_salaries', 'slowing_growth_plans', 'improving_studio_process', 
                 'investing_in_tools', 'lengthening_game_time ', 'can_not_solve_talent_issues', 
                 'no_talent_issue', 'others']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Yes', '0.0': 'No'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        SM12dr_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    SM12dr_df.head()
    
    """One column (SM12dr8oe) is skip in between """
    
    # SM12e
    SM12e = data[['SM12e']]
    
    merged_column = SM12e['SM12e'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'100%', '2.0':'90-99%', '3.0':'80-89%', '4.0':'60-79%', '5.0':'40-59%','6.0':'20-39%', '7.0':'Less than 20%'}
    
    SM12e_company = DM1Merged.replace({'SM12e':codedValues})
    SM12e_company.rename(columns={'SM12e': 'male(%)'}, inplace=True)
    SM12e_company.head()
    
    # SM13
    SM13 = data[['SM13']]
    
    merged_column = SM13['SM13'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Yes', '2.0':'No'}
    
    SM13_company = DM1Merged.replace({'SM13':codedValues})
    SM13_company.rename(columns={'SM13': 'studio_making_adequate_investments'}, inplace=True)
    SM13_company.head()
    
    #SM13a
    SM13a = data[['SM13a']]
    
    merged_column = SM13a['SM13a'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Yes', '2.0':'No', '3.0':'I don’t have visibility'}
    
    SM13a_company = DM1Merged.replace({'SM13a':codedValues})
    SM13a_company.rename(columns={'SM13a': 'technical_dept_is_your_title'}, inplace=True)
    SM13a_company.head()
    
    # SM13b
    SM13b = data[['SM13b']]
    
    merged_column = SM13b['SM13b'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Not at all', '2.0':'Very poorly', '3.0':'Basic understanding', '4.0':'Very well', '5.0':'Not applicable'}
    
    SM13b_company = DM1Merged.replace({'SM13b':codedValues})
    SM13b_company.rename(columns={'SM13b': 'ROI_understanding'}, inplace=True)
    SM13b_company.head()
    
    # SM13cr1 to SM13cr7
    
    
    columnDict = {'1':'Game Art ', 
                  '2':'Game Programming ',
                  '3':'Game Design ', 
                  '4':'Software engineers',
                  '5':'Testing & QA',
                  '6': 'Data Analytics ',
                  '7': 'Studio IT infrastructure',
                  '' :''}
    
    SM13cr = data[['SM13cr1', 'SM13cr2', 'SM13cr3', 'SM13cr4',
                 'SM13cr5','SM13cr6','SM13cr7']]
    
    SM13cr_orders = pd.DataFrame()
    
    for i, row in SM13cr.iterrows():
      row = np.asarray(row)
      row = np.where(np.isnan(row), '', row.astype(int).astype(str))
      row = row.tolist()
      rowResulted = [''] * len(row)
    
      for index, value in enumerate(row):
          if value == '1':
              rowResulted[0] = index+1
          elif value == '2':
              rowResulted[1] = index+1
          elif value == '3':
              rowResulted[2] = index+1
          elif value == '4':
              rowResulted[3] = index+1
          elif value == '5':
              rowResulted[4] = index+1
          elif value == '6':
              rowResulted[5] = index+1
          elif value == '7':
              rowResulted[6] = index+1
          elif value == ' ':
              rowResulted[index] = ' '
      result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
    
      SM13cr_orders.at[i, "prioritized_department_for_investment(most to least)"] = ', '.join(result_list)
    
    SM13cr_orders.head()
    
    # SM13d
    
    
    SM13d = data[['SM13d']]
    
    merged_column = SM13d['SM13d'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Seat-based licenses ', '2.0':'Consumption based ', '3.0':'Capacity based ', '4.0':'No strong preference'}
    
    SM13d_company = DM1Merged.replace({'SM13d':codedValues})
    SM13d_company.rename(columns={'SM13d': 'prefered_pricing_model'}, inplace=True)
    SM13d_company.head()
    
    # SM15a
    SM15a = data[['SM15a']]
    
    merged_column = SM15a['SM15a'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Yes, it is viable for us today', '2.0':'Yes, it may be viable in 1-3 years', '3.0':'Yes, it may be viable in the far future (5+ years)', '4.0':'No, I don’t think it is viable for my studio'}
    
    SM15a_company = DM1Merged.replace({'SM15a':codedValues})
    SM15a_company.rename(columns={'SM15a': 'looking_web_browser-based_technology'}, inplace=True)
    SM15a_company.head()
    
    # SM15b
    SM15b = data[['SM15b']]
    
    merged_column = SM15b['SM15b'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Yes', '2.0':'No, but interested', '3.0':'No, not interested'}
    
    SM15b_company = DM1Merged.replace({'SM15b':codedValues})
    SM15b_company.rename(columns={'SM15b': 'releasing_support_for_cloud_streaming'}, inplace=True)
    SM15b_company.head()
    
    # SM15c
    SM15c = data[['SM15c']]
    
    merged_column = SM15c['SM15c'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'Yes', '2.0':'No, but interested', '3.0':'No, not interested'}
    
    SM15c_company = DM1Merged.replace({'SM15c':codedValues})
    SM15c_company.rename(columns={'SM15c': 'adopting_cloud_infrastructure'}, inplace=True)
    SM15c_company.head()
    
    # SM15d
    SM15d = data[['SM15d']]
    
    merged_column = SM15d['SM15d'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1.0':'No benefit', '2.0':'Very little benefit', '3.0':'Some benefit', '4.0':'Very beneficial', '5.0':'Not applicable'}
    
    SM15d_company = DM1Merged.replace({'SM15d':codedValues})
    SM15d_company.rename(columns={'SM15d': 'how_beneficial-cloud_infrastructure'}, inplace=True)
    SM15d_company.head()
    
    
    
    
    
    """# SECTION: State of Technology
    
    ### QCheck2
    """
    
    # QCheck2
    
    STQCheck2 = data[['QCHECK2']]
    
    merged_column = STQCheck2['QCHECK2'].astype(str)
    
    DM1Merged = pd.DataFrame(merged_column)
    
    codedValues = {'1':'Strongly disagree', '2':'Somewhat disagree', '3':'Neither agree nor disagree', '4':'Somewhat agree', '5':'Strongly agree'}
    
    STQCheck2_company = DM1Merged.replace({'QCHECK2':codedValues})
    STQCheck2_company.rename(columns={'QCHECK2': 'qualityCheck2'}, inplace=True)
    STQCheck2_company.head()
    
    """### ST7"""
    
    # ST7
    ST7 = data[['ST7']]
    merged_column = ST7['ST7'].astype(str)
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1':'Very satisfied ', '2':'Satisfied ', '3':'Unsatisfied ', '4':'Very unsatisfied '}
    ST7_company = DM1Merged.replace({'ST7':codedValues})
    ST7_company.rename(columns={'ST7': 'satisfaction'}, inplace=True)
    ST7_company.head()
    
    # ST7b br1 1 to 5. Buying tools
    
    # List of columns to replace values
    merged_column = ['ST7br1', 'ST7br2', 'ST7br3', 'ST7br4', 'ST7br5']  # Add more column names as needed
    
    # Create a new DataFrame to store the replaced columns
    ST7br_df = pd.DataFrame()
    columName = ['buy_studio:improve_game', 'buy_studio:reduce_cost ', 'buy_studio:improve_technology', 
                 'buy_studio:standardize_technology', 'buy_studio:avoid_technical_debt']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Yes', '0.0': 'No'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        ST7br_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    ST7br_df.head()
    
    
    
    # ST7b orders 1 to 5 Buy tools
    
    columnDict = {'1':'Improve game time-to-market', 
                  '2':'Reduce the cost of game development',
                  '3':'Improve our technology’s stability', 
                  '4':'Standardize the technology we use',
                  '5':'Avoid long term technical debt',
                  '' :''}
    
    ST7b = data[['ST7b_Orderr1', 'ST7b_Orderr2', 'ST7b_Orderr3', 'ST7b_Orderr4',
                 'ST7b_Orderr5']]
    
    ST7b_orders = pd.DataFrame()
    
    for i, row in ST7b.iterrows():
      row = np.asarray(row)
      row = np.where(np.isnan(row), '', row.astype(int).astype(str))
      row = row.tolist()
      rowResulted = [''] * len(row)
    
      for index, value in enumerate(row):
          if value == '1':
              rowResulted[0] = index+1
          elif value == '2':
              rowResulted[1] = index+1
          elif value == '3':
              rowResulted[2] = index+1
          elif value == '4':
              rowResulted[3] = index+1
          elif value == '5':
              rowResulted[4] = index+1
          elif value == ' ':
              rowResulted[index] = ' '
      result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
    
      # Store the resulted list values in a single column of ST7b_orders
      ST7b_orders.at[i, "reason_to_buy_studio(most to least)"] = ', '.join(result_list)
    
    ST7b_orders
    
    
    
    # ST7c  br 1 to 5 Build tools
    
    # List of columns to replace values
    merged_column = ['ST7cr1', 'ST7cr2', 'ST7cr3', 'ST7cr4', 'ST7cr5']  # Add more column names as needed
    
    # Create a new DataFrame to store the replaced columns
    ST7cr_df = pd.DataFrame()
    columName = ['build_studio:improve_game', 'build_studio:reduce_cost ', 'build_studio:improve_technology', 
                 'build_studio:standardize_technology', 'build_studio:avoid_technical_debt']
    # Iterate over each column
    for i, column in enumerate(merged_column):
        merged_column = data[column].astype(str)
        DM1Merged = pd.DataFrame(merged_column)
        codedValues = {'1.0': 'Yes', '0.0': 'No'}
        replaced_column = DM1Merged.replace({column: codedValues})
        
        # Customized column name for the replaced column
        new_column_name =  columName[i] # Customize as desired
        
        # Add the replaced column to the new DataFrame
        ST7cr_df[new_column_name] = replaced_column
    
    # Print the updated DataFrame with replaced columns
    ST7cr_df.head()
    
    # ST7c  _order 1 to 5 Build tools
    columnDict = {'1':'Avoid relying on vendors for software support', 
                  '2':'The costs of buying software is expensive',
                  '3':'There is a risk of software vendors going out of business', 
                  '4':'Off the shelf software has limited functionality',
                  '5':'Off the shelf tools have a steep learning curve',
                  '' :''}
    
    
    ST7c = data[['ST7c_Orderr1', 'ST7c_Orderr2', 'ST7c_Orderr3', 'ST7c_Orderr4',
                 'ST7c_Orderr5']]
    
    ST7c_orders = pd.DataFrame()
    
    for i, row in ST7c.iterrows():
      row = np.asarray(row)
      row = np.where(np.isnan(row), '', row.astype(int).astype(str))
      row = row.tolist()
      rowResulted = [''] * len(row)
    
      for index, value in enumerate(row):
          if value == '1':
              rowResulted[0] = index+1
          elif value == '2':
              rowResulted[1] = index+1
          elif value == '3':
              rowResulted[2] = index+1
          elif value == '4':
              rowResulted[3] = index+1
          elif value == '5':
              rowResulted[4] = index+1
          elif value == ' ':
              rowResulted[index] = ' '
      result_list = [columnDict[str(element)] for element in rowResulted if str(element) in columnDict]
      
      # Store the resulted list values in a single column of ST7b_orders
      ST7c_orders.at[i, "reason_to_build_studio(most to least)"] = ', '.join(result_list)
    
    ST7c_orders
    
    
    
    # ST7d
    ST7d = data[['ST7d']]
    merged_column = ST7d['ST7d'].astype(str)
    DM1Merged = pd.DataFrame(merged_column)
    codedValues = {'1':'Increase', '2':'Decrease', '3':'No change'}
    ST7d_company = DM1Merged.replace({'ST7d':codedValues})
    ST7d_company.rename(columns={'ST7d': 'off-the-shelf_tools:increase_or_decrease?'}, inplace=True)
    ST7d_company.head()
    
    """## Cleaned Dataset"""
    
    # Horizontal merge using pd.concat()
    cleaned_last_three_sections = pd.concat([PL8r_df, PL8_orders, PL8a_company, PL8b_company, PL9_company, PL9a_company, PL9b_company, PL10_company, PL10a_company,PL11_company, PL11a_company, PL11b_company, PL11c_company, PL11d_company, PL11e_company, PL12r_df, PL12ar_df, SM11_company, SM11ar_df, SM11b_df, SM11c_company, SM12_company, SM12_df, SM12a_orders, SM12b_df, SM12b_orders, SM12c_company, SM12dr_df, SM12e_company, SM13_company, SM13a_company, SM13b_company, SM13cr_orders, SM13d_company, SM15a_company, SM15b_company, SM15c_company, SM15d_company, STQCheck2_company, ST7_company, ST7br_df, ST7b_orders, ST7cr_df,ST7b_orders, ST7c_orders,ST7d_company ], axis=1)
    
    # Merging the final dataframe
    finalDf = pd.concat([cleanedData, cleaned_last_three_sections], axis = 1)
    
    finalDf.to_csv(fileLocation + 'cleaned_surveyData.csv')
    
##### WHILE CALLING THE FUNCTION, PLEASE CHANGE LOCATION and FILENAME ACCORDINGLY,
    #### MAKE SURE TO ADD THE FILENAME WITH EXTENSION (.xlsx)
    #### GIVE THE LOCATION as this ---->>> r'folder_location'
cleanData(r'D:/', 'ORD-803734-T8H9_Partial_Excel_051523.xlsx')