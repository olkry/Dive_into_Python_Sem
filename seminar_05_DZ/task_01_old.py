def get_file_info(file_path):
    parts = file_path.rsplit('/', 1)
    path = parts[0] + '/' if len(parts) > 1 else ''

    file_name_with_extension = parts[-1] if len(parts) > 1 else parts[0]
    name, extension = file_name_with_extension.rsplit('.', 1) if '.' in file_name_with_extension else (
    file_name_with_extension, '')

    return path, name, '.' + extension if extension else ''