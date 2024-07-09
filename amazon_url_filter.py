from urllib.parse import urlparse, parse_qs, urlencode
import random

def get_condition_ids(category):
    # Different categories might use different condition IDs
    if category == 'kitchen':
        return {
            'new': '6358196011',
            'used': '6358198011',
            'renewed': '17875379011'
        }
    else:
        # Default condition IDs for other categories
        return {
            'new': '6461716011',
            'used': '6461718011',
            'renewed': '17871321011'
        }

def add_condition_filter(url, condition='used'):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Parse the query string
    query_params = parse_qs(parsed_url.query)
    
    # Get the category
    category = query_params.get('i', [''])[0]
    
    # Get the appropriate condition IDs for this category
    condition_ids = get_condition_ids(category)
    
    # Get the appropriate condition ID
    condition_id = condition_ids.get(condition.lower(), condition_ids['used'])
    
    # Modify the 'rh' parameter
    rh_params = query_params.get('rh', [''])[0].split(',')
    rh_params = [p for p in rh_params if not p.startswith('p_n_condition-type')]
    rh_params.append(f"p_n_condition-type:{condition_id}")
    query_params['rh'] = [','.join(rh_params)]
    
    # Update or add rnid
    query_params['rnid'] = ['6358194011']
    
    # Update ref parameter
    ref_parts = query_params.get('ref', [''])[0].split('_')
    if len(ref_parts) >= 4:
        ref_parts[-2] = 'p_n_condition-type'
        ref_parts[-1] = '2'
    query_params['ref'] = ['_'.join(ref_parts)]
    
    # Generate a new qid if it doesn't exist
    if 'qid' not in query_params:
        query_params['qid'] = [str(random.randint(1000000000, 9999999999))]
    
    # Remove 'ds' parameter as it seems to be a session-specific parameter
    query_params.pop('ds', None)
    
    # Reconstruct the query string
    new_query = urlencode(query_params, doseq=True)
    
    # Reconstruct the URL
    new_url = parsed_url._replace(query=new_query).geturl()
    
    # Replace any '&amp;' with '&' (Amazon sometimes uses these interchangeably)
    new_url = new_url.replace('&amp;', '&')
    
    return new_url

def get_all_condition_urls(url):
    conditions = ['new', 'used', 'renewed']
    filtered_urls = {condition: add_condition_filter(url, condition) for condition in conditions}
    filtered_urls['original'] = url
    return filtered_urls

def main():
    while True:
        url = input("Please enter an Amazon URL (or 'quit' to exit): ")
        if url.lower() == 'quit':
            break
        
        results = get_all_condition_urls(url)
        
        print("\nHere are your filtered URLs:")
        for condition, filtered_url in results.items():
            print(f"\n{condition.capitalize()}:")
            print(filtered_url)
        
        print("\n")

if __name__ == "__main__":
    main()