## Post-processing on Templates

### Tasks

1. Remove the `output_dir` in the Jinja variables & `if __name__ == "__main__"` guard (if any). This is because of the old design of validation needs to save the inference results on disk, but in the new design we have deprecated it, so no output path is needed. 

2. Add the demo data dir to the template. However, we don't remove the hardcoded path, we fill it with real demo data dir path when calling the API. Since if we use the relative path `Path(__file__)` to deduce at post-processing time, then the default value is no longer a literal string, which will cause errors in rendering. Since we need `image = "{{image}}"`  to render, but the relative is a path object. 

3. Add `repo_id` and `device` at the header of the template if such variables are not presented / have wrong default values, since we have observed that some templates do not have default values for these two variables defined at header. 

4. Add the original `README.md` file back.

### Scripts

- `remove_old_output.py` for Task 1.
- `ensure_jinja_variables.py` for Task 3.
- `get_modelcard.py` for Task 4.