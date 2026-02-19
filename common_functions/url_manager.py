import common_variables

class URLManager:
    """
    Centralizes URL retrieval logic to avoid scattered getattr calls.
    """

    @staticmethod
    def get_url(key_suffix: str, funnel_prefix: str = None) -> str:
        """
        Retrieves a URL from common_variables.
        
        Args:
            key_suffix (str): The variable name (e.g., 'ad_live_opt_in_url') or suffix.
            funnel_prefix (str, optional): The funnel prefix (e.g., 'ad', 'lg'). 
                                           Used to construct the variable name if key_suffix is not found directly.
        
        Returns:
            str: The URL value from common_variables.
        
        Raises:
            AttributeError: If the constructed variable name doesn't exist in common_variables.
        """
        # 1. Try exact match first (e.g. "ad_live_opt_in_url" or "welcome_page_url")
        if hasattr(common_variables, key_suffix):
            return getattr(common_variables, key_suffix)

        # 2. If prefix is provided, try constructing the key (e.g. prefix="ad", suffix="opt_in_url" -> "ad_opt_in_url")
        if funnel_prefix:
            variable_name = f"{funnel_prefix}_{key_suffix}"
            # Clean up double underscores if any
            variable_name = variable_name.replace("__", "_")
            
            if hasattr(common_variables, variable_name):
                return getattr(common_variables, variable_name)

        # 3. Failure
        error_msg = f"URL configuration error: Variable '{key_suffix}' not found in common_variables.py"
        if funnel_prefix:
             error_msg += f" (also tried '{funnel_prefix}_{key_suffix}')"
        
        raise AttributeError(error_msg)

    @staticmethod
    def get_funnel_url(funnel_name: str, page_type: str) -> str:
        """
        Helper for specific funnel pages like opt-in, sales, etc.
        Example: get_funnel_url('ad_live', 'opt_in_url') -> common_variables.ad_live_opt_in_url
        """
        variable_name = f"{funnel_name}_{page_type}"
        try:
            return getattr(common_variables, variable_name)
        except AttributeError:
            raise AttributeError(f"Funnel URL error: Variable '{variable_name}' not found in common_variables.py")